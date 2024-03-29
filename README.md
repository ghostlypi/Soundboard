
# Soundboard

Soundboard is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Soundboard.
For windows:

```batch
py -m pip install Soundboard
```
For Mac/Linux:
```bash
pip3 install Soundboard
```

## Usage

```python
import Soundboard

arr1 =[Soundboard.C ] #Note/Frequency
arr2 =[4   ] #Amplitude
arr3 =[100 ] #Duration
Soundboard.render(arr1,arr2,arr3,"Test1")
arr1 =[Soundboard.E ] #Note/Frequency
arr2 =[4   ] #Amplitude
arr3 =[100 ] #Duration
Soundboard.render(arr1,arr2,arr3,"Test2")
arr1 =[Soundboard.G ] #Note/Frequency
arr2 =[4   ] #Duration
arr3 =[100 ] #Amplitude
Soundboard.render(arr1,arr2,arr3,"Test3")
Soundboard.add("Test1","Test2","Test4")
Soundboard.add("Test3","Test4","Combotest")
Soundboard.make("Combotest")
```
### Check our [GitHub](https://github.com/ghostlypi/Soundboard)
## Documentation

### Render (Soundboard.Soundboard)
```python
Soundboard.render(frequency,duration,amplitude,filename)
```
takes in an array of frequencies, and array of duration, and an array of amplitudes and a string filename
#### Note: The arrays must be of equal length or else the program will error.

### Add (Soundboard.Soundboard)
```python
Soundboard.add(track1,track2,output_file_name)
```
takes in 2 track build files and outputs a new build file that includes both tracks merged together
#### Note: You have to "make" the added files or else you will not be able to play the sound
### Build (Soundboard.Soundboard)
```python
Soundboard.build(arr, name)
```
takes in an 2 dimensional array - an sequence of note arrays containing 3 values, frequency, duration, and amplitude
```python
Soundboard.build([[frequency,duration,amplitude], ...], name)
```

#### Note: The build will fail with an error if all 3 values are not filled in for each and every note.
#### Note: Build will return a file called "<name>.sbld" containing numerical values for speaker positions

### Make (Soundboard.Soundboard)
```python
Soundboard.make(filename)
```
takes in a filename
#### Note: Make will fail if there is no "Build.txt" in the current directory.

### Unmake (Soundboard.Decomposition)
```python
Soundboard.unmake(filename)
```

given a .wav file, this will output the build output
#### Note: unmake only works on 16 bit integer wav files. Other formats are currently unsupported.

### Spectrum (Soundboard.Decomposition)
```python
Soundboard.spectrum(filename)
```

given a .sbld file, this will output the spectrum

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
