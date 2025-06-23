# arduino-led
Questo progetto permette di accendere e spegnere un LED collegato al pin 13 di un Arduino Uno tramite un'interfaccia grafica in Python.

## Requisiti

- Arduino Uno (o compatibile)
- Python 3
- Libreria `pyserial`
- Libreria `tkinter` (di solito inclusa con Python)
- Modificare la porta seriale nel file `PYTHON.py` (es. `COM3` su Windows, `/dev/ttyACM0` su Linux).
```bash
python PYTHON.py
