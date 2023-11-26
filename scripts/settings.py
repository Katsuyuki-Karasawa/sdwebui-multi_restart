import modules.scripts as scripts
import gradio as gr
import os

from modules import shared
from modules import script_callbacks

# def on_ui_settings():
#         section = ("sampler-params", "Sampler parameters")
#         shared.opts.add_option(
#                 "restart_steps", 
#                 OptionInfo(
#                         1.0,
#                         "restart_steps for Multi Restart",
#                         gr.Slider,
#                         {"minimum": 6.0, "maximum": 100.0, "step": 1.0},
#                         infotext='Eta'
#                         ).info("Values of restart_steps for Multi Restart"),
#         )

def on_ui_settings():
    section = ('multi_restart', "Multi Restart")
    shared.opts.add_option("restart_steps", OptionInfo(6, label="restart_steps for Multi Restart", component=gr.Slider, component_args={"minimum": 0, "maximum": 100, "step": 1}, section=section))

script_callbacks.on_ui_settings(on_ui_settings)
