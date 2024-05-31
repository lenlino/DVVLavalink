import os
from typing import Annotated

import aiofiles
from fastapi import FastAPI, UploadFile, File
from httpcore import ReadTimeout

app = FastAPI()
counter = 0

@app.post("/send_wav")
async def send_wav(file: Annotated[bytes, File()]):
    global counter
    counter += 1
    if counter > 300:
        counter = 0
    filename = "temp" + str(counter) + ".wav"
    dir = os.path.dirname(os.path.abspath(__file__)) + "/voice/" + filename
    try:
        async with aiofiles.open(dir,
                                 mode='wb') as f:
            await f.write(file)
        return dir
    except ReadTimeout:
        return "error"
