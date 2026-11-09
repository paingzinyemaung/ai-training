import gradio as gr
import joblib
import pandas as pd

# load the model
model = joblib.load('model/wine_model.joblib')

def predict_wine_quality(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
    input_data = pd.DataFrame({
        'fixed acidity': [fixed_acidity],
        'volatile acidity': [volatile_acidity],
        'citric acid': [citric_acid],
        'residual sugar': [residual_sugar],
        'chlorides': [chlorides],
        'free sulfur dioxide': [free_sulfur_dioxide],
        'total sulfur dioxide': [total_sulfur_dioxide],
        'density': [density],
        'pH': [pH],
        'sulphates': [sulphates],
        'alcohol': [alcohol]
    })

    prediction = model.predict(input_data)
    return round(prediction[0], 2)


# ---------- result card ----------
def result_card(score=None):
    if score is None:
        return """
        <div class="result empty">
            <div class="emoji">🍷</div>
            <div class="hint">Enter the values and press <b>Predict Quality</b></div>
        </div>"""

    # limit value between 0 and 10 (clamp)
    score = max(0, min(10, score))
    if score >= 7:
        label, c1, c2 = "Excellent 🌟", "#059669", "#34d399"
    elif score >= 6:
        label, c1, c2 = "Good 👍", "#65a30d", "#a3e635"
    elif score >= 5:
        label, c1, c2 = "Average 🙂", "#d97706", "#fbbf24"
    else:
        label, c1, c2 = "Poor 👎", "#e11d48", "#fb7185"

    return f"""
    <div class="result">
        <div class="small">Predicted Quality</div>
        <div class="score" style="background:linear-gradient(135deg,{c1},{c2});
             -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            {score:.2f}<span> / 10</span>
        </div>
        <div class="badge" style="background:{c1}">{label}</div>
        <div class="bar"><div style="width:{score * 10}%;background:linear-gradient(90deg,{c1},{c2})"></div></div>
    </div>"""


def run(*values):
    return result_card(predict_wine_quality(*values))


# ---------- inputs (label, default value) ----------
FIELDS = [
    ("Fixed Acidity", 7.0),
    ("Volatile Acidity", 0.27),
    ("Citric Acid", 0.36),
    ("Residual Sugar", 20.7),
    ("Chlorides", 0.045),
    ("Free Sulfur Dioxide", 45.0),
    ("Total Sulfur Dioxide", 170.0),
    ("Density", 1.001),
    ("pH", 3.0),
    ("Sulphates", 0.45),
    ("Alcohol", 8.8),
]

def reset():
    return [v for _, v in FIELDS] + [result_card()]


# ---------- design (soft blue, light, fits ONE screen) ----------
css = """
/* ===== soft blue page background ===== */
html, body {
    min-height: 100vh;
    color-scheme: light;
    background:
        radial-gradient(circle at 8% 10%,  rgba(147,197,253,.65), transparent 45%),
        radial-gradient(circle at 92% 88%, rgba(196,181,253,.55), transparent 45%),
        radial-gradient(circle at 85% 8%,  rgba(251,207,232,.45), transparent 40%),
        linear-gradient(160deg, #eaf3ff 0%, #dbe9ff 55%, #e8e6ff 100%) !important;
    background-attachment: fixed !important;
}
gradio-app, .gradio-container, .main, .wrap {background: transparent !important;}
.gradio-container {
    max-width: 1150px !important; margin: auto !important;
    min-height: auto !important;
    padding: clamp(8px, 6vh, 56px) 20px 8px !important;
}
footer {display: none !important;}

/* ===== force light colors ===== */
:root, .dark, .gradio-container {
    --body-text-color: #1e293b !important;
    --block-label-text-color: #475569 !important;
    --block-title-text-color: #475569 !important;
    --block-background-fill: transparent !important;
    --block-border-color: transparent !important;
    --panel-background-fill: transparent !important;
}
.form, .block {background: transparent !important; border: none !important; box-shadow: none !important;}

/* ===== grid: 4 inputs per row, never wrap ===== */
.card .form {gap: 0 !important;}
.card .row {gap: 14px !important; flex-wrap: nowrap !important; margin-bottom: 14px;}
.card .row > * {min-width: 0 !important;}
.card label span, .card .block-title {
    font-size: .82rem !important; font-weight: 600 !important; color: #475569 !important;
    margin-bottom: 6px !important;
}

/* ===== input boxes: always visible (white box + blue border) ===== */
.card input[type=number], .card input {
    background: #ffffff !important;
    border: 1.5px solid #bcd0f5 !important;
    border-radius: 12px !important;
    color: #1e293b !important;
    font-size: 1rem !important; font-weight: 600 !important;
    padding: 11px 14px !important;
    box-shadow: 0 2px 6px rgba(59,130,246,.08) !important;
    transition: border-color .15s, box-shadow .15s;
}
.card input:hover {border-color: #8fb2f0 !important;}
.card input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 4px rgba(59,130,246,.18) !important;
    outline: none !important;
}

/* ===== header ===== */
#header {text-align: center; padding: 0 0 clamp(10px, 2.5vh, 26px);}
#header h1 {
    font-size: 2.3rem; margin: 0; font-weight: 800;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #ec4899);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
#header p {color: #64748b; margin: 6px 0 0; font-size: 1rem;}

/* ===== cards ===== */
.card {
    background: rgba(255,255,255,0.72) !important;
    border: 1px solid rgba(255,255,255,0.95) !important;
    border-radius: 24px !important;
    padding: 24px 26px !important;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 10px 32px rgba(59,130,246,.15) !important;
}
.card h3 {margin: 0 0 14px; color: #1e293b; font-size: 1.1rem;}

/* ===== buttons ===== */
#predict {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
    border: none !important; color: #fff !important;
    font-size: 1.05rem !important; font-weight: 700 !important;
    padding: 14px !important; border-radius: 14px !important;
    box-shadow: 0 8px 20px rgba(99,102,241,.35);
}
#predict:hover {filter: brightness(1.08); transform: translateY(-1px);}
#reset {
    background: #eef3ff !important; color: #475569 !important;
    border: 1px solid #c7d7f5 !important; border-radius: 14px !important;
}
#reset:hover {background: #e0e9ff !important;}

/* ===== result card ===== */
.result {
    background: #ffffff; border-radius: 20px; padding: 28px 18px; text-align: center;
    box-shadow: 0 6px 22px rgba(59,130,246,.18);
}
.result .small {color: #94a3b8; font-size: .78rem; letter-spacing: .12em; text-transform: uppercase; font-weight: 700;}
.result .score {font-size: 4.4rem; font-weight: 800; line-height: 1.15; margin: 2px 0 8px;}
.result .score span {font-size: 1.1rem; font-weight: 600; -webkit-text-fill-color: #94a3b8;}
.result .badge {
    display: inline-block; padding: 6px 20px; border-radius: 999px;
    color: #fff; font-weight: 700; font-size: 1rem;
}
.result .bar {height: 9px; border-radius: 8px; background: #e2e8f0; margin-top: 20px; overflow: hidden;}
.result .bar > div {height: 100%; border-radius: 8px;}
.result.empty {background: #f4f8ff; border: 2px dashed #bcd0f5; box-shadow: none; padding: 40px 18px;}
.result .emoji {font-size: 3.6rem;}
.result .hint {color: #64748b; margin-top: 8px; line-height: 1.5;}

#legend {text-align: center; color: #64748b; font-size: .8rem; margin-top: 2px;}
#footer {text-align: center; color: #94a3b8; font-size: .8rem; padding: 14px 0 4px;}

/* short screens: shrink a little so nothing scrolls */
@media (max-height: 800px) {
    #header h1 {font-size: 1.8rem;}
    .card {padding: 18px 20px !important;}
    .card .row {margin-bottom: 8px;}
    .result {padding: 18px 14px;}
    .result .score {font-size: 3.4rem;}
    .result.empty {padding: 26px 14px;}
}
"""

theme = gr.themes.Base(
    primary_hue="blue",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "sans-serif"],
)

# use instead of Interface
with gr.Blocks(theme=theme, css=css, title="Wine Quality Predictor",
               js="() => document.body.classList.remove('dark')") as demo:

    gr.HTML("""
    <div id="header">
        <h1>🍷 Wine Quality Predictor</h1>
        <p>Enter the chemical data of a white wine to predict its quality score</p>
    </div>""")

    with gr.Row():
        # left: inputs in a 4-column grid
        with gr.Column(scale=3, elem_classes="card"):
            gr.Markdown("### 🧪 Chemical Properties")
            inputs = []
            for i in range(0, len(FIELDS), 4):
                chunk = FIELDS[i:i + 4]
                with gr.Row():
                    for label, value in chunk:
                        inputs.append(gr.Number(label=label, value=value, min_width=0))
                    # empty spacer so the last row keeps the same column width
                    for _ in range(4 - len(chunk)):
                        gr.HTML("")

        # right: result
        with gr.Column(scale=2, elem_classes="card"):
            result = gr.HTML(result_card())
            predict_btn = gr.Button("Predict Quality", elem_id="predict")
            reset_btn = gr.Button("Reset", elem_id="reset")
            gr.HTML('<div id="legend">Below 5 Poor · 5–6 Average · 6–7 Good · 7+ Excellent</div>')

    gr.HTML('<div id="footer">Linear Regression model · Built with Gradio</div>')

    predict_btn.click(run, inputs=inputs, outputs=result)
    reset_btn.click(reset, outputs=inputs + [result])
    # press Enter in any box to predict
    for box in inputs:
        box.submit(run, inputs=inputs, outputs=result)

demo.launch()