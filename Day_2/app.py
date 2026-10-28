import gradio as gr 

# def greet(name):
#     return f'Hello, {name}!'

# demo = gr.Interface(
#     fn = greet,
#     inputs = gr.Textbox(label = "Enter your name"),
#     outputs = gr.Textbox(label = "Greeting"),
#     title = "My first Gradio App"
# )

# demo.launch()

# two numerical input
def calculate_total(a, b):
    return a + b

demo = gr.Interface(
    fn = calculate_total,
    inputs = [
        gr.Number(label = "First Number"),
        gr.Number(label = "Second Number")
    ],
    outputs = gr.Number(label = "Total"),
    title = "Simple Calculator"
)

demo.launch()