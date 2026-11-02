import gradio as gr 

def calculate_total(a, b):
    return a + b

demo = gr.Interface(
    fn = calculate_total,
    inputs = [
        gr.Number(label = "Enter first number"),
        gr.Number(label = "Enter Second number"),
    ],
    outputs = gr.Number(label = 'Total'),
    title = 'Simple Calculator'
)

demo.launch()