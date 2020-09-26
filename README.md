<img width="64" src="img/logo.png">
<h3>ISO8583 Dlib Parser</h3>
<p>
Parser String to JSON for ISO8583 Package
</p>
<p>
<a href="https://www.python.org/">
    <img src="https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square"  alt="python badge">
</a>
</p>

This package has been developed  with a cookiecutter made for me in: https://github.com/ActivandoIdeas/Python-Package-Cookiecutter

## Docs

Full docs ISO: https://github.com/eocode/ISO8583-Dlib/blob/master/8583.pdf

About ISO Links: 

* https://es.wikipedia.org/wiki/ISO_8583
* https://www.chileoffshore.com/es/interesting-articles/115-todo-sobre-iso8583
* http://j8583.sourceforge.net/es/iso8583.html

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
# Set true to generate a data.json file with parser message
print(data.get_json(save=True))
```

The output is a json

```json
{
    "literal": "ISO",
    "header": {
        "Complete_header": "026000070",
        "Product_indicator": {
            "value": "02",
            "description": "POS"
        },
        "Release_number": {
            "value": "60",
            "description": "DEFAULT"
        },
        "Status": {
            "value": "000",
            "description": "Undetermined"
        },
        "Originator_code": {
            "value": "7",
            "description": "Interchange"
        },
        "Responder_code": {
            "value": "0",
            "description": "Undetermined"
        }
    },
    "mti": {
        "value": "0200",
        "description": "Financial transaction request"
    },
    "primary_bitmap": "B23E842128A1801A",
    "...": "..."
}
```

Full output message: https://github.com/eocode/ISO8583-Dlib/blob/master/data.json

## Test this project

```sh
pip install pytest
pytest
```

## Think use

Easy library for use, create an specific API with your favorite framework and integrate with other systems

## To Do

* Validate in real use
* Valid output
* Complement json rules to process all Data Elements
* Add logic for variable Data Elements
* Add other output formats
* Add other input formats
* Make validations with a library as https://pydantic-docs.helpmanual.io/usage/validators or a simple implementation

## How to contribute

Read CONTRIBUTTING.md file and make an issue and send a PR to improve