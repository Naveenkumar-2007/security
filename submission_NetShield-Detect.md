# Project Title
Advanced Network Security Threat Detector (NetShield-Detect)

# Team / Author
Naveen Kumar
Email: naveenkumarchapala123@gmail.com
Phone: +91-8897464729
State: Tamil Nadu
College: Saveetha Institute of Medical and Technical Sciences
Current Year: 3rd Year
UID: b57b300f-a70d-403b-90dc-77cdcd960e0a

# Problem Statement
Phishing websites and malicious network artifacts remain a major source of cyberattacks. Security teams and everyday users lack a simple, fast tool to analyze URL and network features at scale and flag likely phishing or malicious sites from CSV datasets.

# Solution Overview
A Streamlit web application powered by a trained machine learning model that classifies URLs/websites as legitimate or phishing using URL and network/website features. Users upload a CSV, the app preprocesses it, runs the model, stores results in MongoDB, and provides downloadable CSVs. The app adds a `predicted_column` where 1 = Legitimate and 0 = Phishing. Live demo: https://security-clou.onrender.com/

# How OpenAI APIs Will Be Used
- Generate human-readable explanations per prediction (why a URL was flagged).
- Summarize large CSV outputs into short, prioritized reports (top suspicious entries).
- Provide remediation tips and a simple conversational assistant in the UI for non-technical users.
- Optionally assist with safe, validated synthetic data generation for model augmentation.

# Feasibility & Scaling Plan
- Short term (MVP): Harden current Streamlit UI, add textual explanations via OpenAI, and prepare submission assets.
- Mid term: Move OpenAI calls to a secure server-side endpoint, implement PII stripping, add background processing for large CSVs, add basic authentication and logging.
- Scale: Deploy backend on a managed cloud (Render/AWS/GCP), use a managed database, implement job queues (Celery/RQ), rate limiting and cost monitoring for API usage, and a model retraining pipeline driven by performance logs.

# Demo & Source Code
- Live demo: https://security-clou.onrender.com/
- GitHub: https://github.com/Naveenkumar-2007/Advanced-Network-Security-Threat-Detector

# Output Screenshot (not included)
- This PDF version does NOT include the screenshot. Insert your screenshot file (security_app_output.png) into the PDF if you want a visual preview.
- Suggested caption when you add the image: "Streamlit app preview — CSV uploaded, sample rows displayed in 'Uploaded Data', and 'Prediction Results' table showing model outputs."

# Files to include in Google Drive (suggested)
- submission_NetShield-Detect.pdf  <-- final one-page PDF (this file)
- security_app_output.png         <-- screenshot (Image 1) (optional)
- predictions_sample.csv          <-- sample predictions CSV (optional)
- link.txt                        <-- contains live demo & GitHub links (optional)

# Declaration
I confirm that this idea is original and created by our team. I agree to the rules and terms of the Buildathon. I will not submit passwords or sensitive data through Google Forms.

# Google Drive & Upload Instructions
1. Create a folder in Google Drive and place the final PDF and the screenshot (optional) inside.
2. Set folder permission: "Anyone with the link → Viewer".
3. Use these filenames for clarity:
   - submission_NetShield-Detect.pdf
   - security_app_output.png
4. Copy the Drive sharing link and paste it into the Buildathon form's "Upload Submission File (Google Drive Link)" field.