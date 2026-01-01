import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs="text", # text / image / audio
    outputs="text" # text / image / label
)


demo.launch(
    server_name="0.0.0.0",
    server_port=7860
)