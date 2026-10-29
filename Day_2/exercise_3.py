import gradio as gr 

def student_summary(name, study_hours, attendance):
    summary = (
        f"### Student Summary\n\n"
        f"**Student Name:** {name}\n\n"
        f"**Study Hours:** {study_hours}\n\n"
        f"**Attendance Rate:** {attendance}%"
    )
    return summary

demo = gr.Interface(
    fn = student_summary,
    inputs = [
        gr.Textbox(
            label = "Student Name",
            placeholder = "Enter your name..."
        ),
        gr.Number(label = "Study Hours"),
        gr.Slider(label = "Attendance Percentage")
    ],
    outputs = gr.Markdown(label = "Summary Output"),
    title = "Student Record"
)

demo.launch()