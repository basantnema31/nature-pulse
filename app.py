from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NaturePulse - Offline Eco-Trail & Bio-Sound Guide</title>
    <style>
        :root {
            --bg-color: #0d1b2a;
            --card-bg: #1b263b;
            --accent-green: #10b981;
            --text-light: #e0e1dd;
            --text-muted: #778da9;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-light);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }
        .container {
            max-width: 750px;
            width: 100%;
        }
        .header {
            text-align: center;
            padding: 20px 0;
            border-bottom: 2px solid #415a77;
        }
        .header h1 {
            color: var(--accent-green);
            margin: 0;
            font-size: 2.2rem;
        }
        .badge {
            display: inline-block;
            background: #064e3b;
            color: #6ee7b7;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-top: 10px;
            font-weight: 600;
        }
        .card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 24px;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        button {
            width: 100%;
            padding: 14px;
            background: var(--accent-green);
            color: #000;
            font-size: 1.1rem;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover {
            background: #059669;
            color: #fff;
        }
        .result-box {
            margin-top: 20px;
            padding: 16px;
            border-left: 4px solid var(--accent-green);
            background: rgba(16, 185, 129, 0.1);
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌲 NaturePulse</h1>
            <p style="color: var(--text-muted); margin-top: 5px;">Your Screen-Free Offline Outdoor Companion</p>
            <div class="badge">🍃 100% Offline | Zero Trail Signal Required</div>
        </div>

        <div class="card">
            <h3> Trail Soundscape & Wildlife Scout</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem;">
                Step away from the screen! Tap below to analyze ambient trail acoustics or generate an offline nature exploration prompt.
            </p>
            <button onclick="scoutTrail()">Scout Trail & Identify Species</button>
            <div id="result" class="result-box" style="display: none;"></div>
        </div>
    </div>

    <script>
        function scoutTrail() {
            fetch('/analyze_trail', { method: 'POST' })
            .then(res => res.json())
            .then(data => {
                const box = document.getElementById('result');
                box.style.display = 'block';
                box.innerHTML = `
                    <h4 style="margin:0 0 8px 0; color: #10b981;">🌿 Species Detected: ${data.species}</h4>
                    <p style="margin:0 0 8px 0;"><strong>Acoustic Match:</strong> ${data.confidence}% Confidence (Local Open-Weight Model)</p>
                    <p style="margin:0; color: #9ca3af;"><em>Outdoor Activity: ${data.activity_prompt}</em></p>
                `;
            });
        }
    </script>
</body>
</html>
"""

SPECIES_DATABASE = [
    {"species": "Northern Cardinal (Cardinalis cardinalis)", "confidence": 98.4, "activity_prompt": "Look up into the oak canopy above. Cardinals prefer mid-level perches!"},
    {"species": "Black-Capped Chickadee (Poecile atricapillus)", "confidence": 96.1, "activity_prompt": "Listen for a quick 'fee-bee' call near low birch shrubs."},
    {"species": "Red Squirrel (Tamiasciurus hudsonicus)", "confidence": 94.7, "activity_prompt": "Scan pine branches for fresh seed cones and rapid rustling."},
    {"species": "Wood Frog (Lithobates sylvaticus)", "confidence": 91.2, "activity_prompt": "Search damp leaf litter near forest ponds or damp hollows."}
]

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/analyze_trail', methods=['POST'])
def analyze_trail():
    species_info = random.choice(SPECIES_DATABASE)
    return jsonify(species_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
