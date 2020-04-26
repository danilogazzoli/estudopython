# -*- coding: utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class LinuxTips(BaseModel):
    canal: str
    msg: str
    dia: int

@app.get("/", response_model=LinuxTips)
def linux_tips():
    return LinuxTips(
            canal="LinuxTips",
            msg = "Exemplo de web API com FastAPI",
            dia = 26
            )








