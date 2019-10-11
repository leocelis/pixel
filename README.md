# Pixel tracking (desktop)
### Installation

Create venv
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Export env vars
```bash
export DB_HOST=your_value
export DB_PORT=your_value
export DB_USER=your_value
export DB_PASSWORD=your_value
```

### Running the server
Run server:
```bash
python3 launcher.py
```
Test pixel:<br /><br />
Go to your browser, and open:
```
http://localhost:8888/pixel/p?ad_id=test&event_name=visit&value=1
```

Debugging:
```bash
tail -f pixel.log
```