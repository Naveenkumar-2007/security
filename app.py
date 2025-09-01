import sys
import os
import certifi
import pandas as pd
import streamlit as st

from dotenv import load_dotenv
from networksecurity.exception.customexception import NetworkSecurityException
from networksecurity.pipeline.training_pipeline import complete_train_pipline
from networksecurity.utilsfile.util  import load_object
from networksecurity.utilsfile.metrics.me import NetworkModel

# MongoDB connection
import pymongo
ca = certifi.where()
load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL_KEY")
client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.trainpipeline import (
    DATA_INGESTION_DATABASE,
    DATA_INGESTION_COLLECTION,
)

database = client[DATA_INGESTION_DATABASE]
collection = database[DATA_INGESTION_COLLECTION]


# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Network Security checker", layout="wide")
st.title("🔐 Network Security using ML ")

menu = ["Home", "Predict"]
choice = st.sidebar.radio("Navigation", menu)

# ---------------- Home ----------------
if choice == "Home":
    st.subheader("Welcome 👋")
    st.write("This is a Netwok security checker ")
    st.write("Use the sidebar to train the model or make predictions.")





# ---------------- Predict ----------------
elif choice == "Predict":
    st.subheader("📌 Upload CSV for Prediction")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("### Uploaded Data")
            st.dataframe(df.head())

            # Load model + preprocessor
            preprocessor = load_object("final_model/preprocessor.pkl")
            final_model = load_object("final_model/model.pkl")
            network_model = NetworkModel(preprocessor=preprocessor, model=final_model)

            # Prediction
            y_pred = network_model.predict(df)
            df['predicted_column'] = y_pred

            # Save predictions
            os.makedirs("prediction_output", exist_ok=True)
            output_path = "prediction_output/output.csv"
            df.to_csv(output_path, index=False)

            st.write("### Prediction Results")
            st.dataframe(df)

            st.success(f"✅ Predictions saved to `{output_path}`")

            # Download button
            st.download_button(
                label="📥 Download Predictions",
                data=df.to_csv(index=False).encode('utf-8'),
                file_name="predictions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")
            raise NetworkSecurityException(e, sys)
