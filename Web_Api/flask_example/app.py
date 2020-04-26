# -*- coding: utf-8 -*-
from flask import Flask

dados = {"canal": "LinuxTips", "msg": "Esta é uma aplicação feita em Flask"}


app = Flask("app")


@app.route("/")
def linux_tips():
    return dados

@app.route("/hello/<nome>/")
def hello(nome):
    return f"<h1>Hello {nome}</h1>"



