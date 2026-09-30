# Name API

Install and run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open <http://127.0.0.1:8000> in a browser. Interactive API documentation is
available at <http://127.0.0.1:8000/docs>.

The API exposes:

- `PUT /putName` with JSON `{ "firstName": "Ada", "surName": "Lovelace" }`
- `GET /getNames` to return every name submitted since startup

Names are stored in memory and reset when the server restarts.
