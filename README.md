<div align="center">
  <img width="64" src="img/isologo.png">
  <h3 align="center">ISO8583 Dlib Parser</h3>
  <p align="center">
    Parser String to JSON for ISO8583 Package
  </p>
  <p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square"  alt="python badge">
    </a>
  </p>
</div>

## Docs

Full docs ISO: https://github.com/eocode/ISO8583-Dlib/blob/master/8583.pdf

Resume Docs and Parser Example

<div align="center">
  <img src="img/ISO%208583.png">
</div>

## How to Install

With pip

    pip install ISO8583-Dlib

## Basic Usage

The entry is a message

```python
from ISO8583-Dlib.parser import Parser

message = "ISO0260000100200B23E842128A1801A00000000100000BC0010000000000070020707203500000013153459070724050707070705161199999999999274231453201761925=2405226096000000000619P0891218        INBURSA CASHBACK      CD MEXICO    001MX0277126834            00010101484016B036PRO1+0000000019B359    00000000000370& 0000700370! C000026              113000       ! C400012 000000021082! Q200002 03! B200158 7FF900008000800080008251FFC4F2FDE21D0000000070020000000000003C00002A48448420070700BE967302000706010A03A4B80200000"
data = Parser(message)
data.iso_8583()
print(data.get_json())
```

The output is a json

```json
{
  "iso": "ISO", 
  "header": "026000010", 
  "mti": "0200", 
  "primary_bitmap": "B23E842128A1801A", 
  "data_elements": ""
}
```

## Test this project

```sh
pip install pytest
pytest
```
