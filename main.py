from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from pathlib import Path
import os

app = FastAPI()

# Directory to store XML files
DATA_DIR = Path("data")
EXAMPLE_XML_PATH = DATA_DIR / "example.xml"

# Create the XML file if it doesn't exist
if not EXAMPLE_XML_PATH.exists():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(EXAMPLE_XML_PATH, "w") as file:
        file.write("""<note>
<to>User</to>
<from>ChatGPT</from>
<heading>Reminder</heading>
<body>This is a reminder to check the FastAPI example project.</body>
</note>""")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/file-response")
def get_file_response():
    # Serve the XML file as a response
    return FileResponse(EXAMPLE_XML_PATH, media_type='application/xml', filename="example.xml")


@app.get("/optimized-file-response")
def get_optimized_file_response():
    # Serve the XML file as an optimized response with custom headers
    file_stats = os.stat(EXAMPLE_XML_PATH)
    headers = {
        'Content-Length': str(file_stats.st_size),
        'Content-Type': 'application/xml',
        'Content-Disposition': 'attachment; filename="example.xml"',
        'Cache-Control': 'no-cache'
    }

    def iterfile():
        with open(EXAMPLE_XML_PATH, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), headers=headers, media_type='application/xml')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
