import gradio as gr
from fastapi import FastAPI
import os

CUSTOM_PATH = os.environ['SHINYPROXY_PUBLIC_PATH']

app = FastAPI()

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

gradio_app = gr.routes.App.create_app(demo) 

app.mount(CUSTOM_PATH, gradio_app)