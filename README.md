# Pixel tracking (desktop)
### Installation

Export env vars
```bash
export DB_HOST=your_value
export DB_PORT=your_value
export DB_USER=your_value
export DB_PASSWORD=your_value
```

### Running the pixel
Run server:
```bash
python3 launcher.py
```
Test pixel:<br />
Go to your browser, and open:
```
http://localhost:8888/pixel/p?ad_id=test&event_name=visit&value=1
```

Debugging:
```bash
tail -f pixel.log
```

### Pixel snippet
