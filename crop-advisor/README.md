# 🌱 Context-Aware Crop Advisory System using RAG and Vector Search

## 📌 Project Overview

This project is an AI-powered **Crop Recommendation System** that provides intelligent, context-aware suggestions for optimal crop selection based on soil and environmental conditions.

Unlike traditional systems that only predict a crop label, this system combines **Machine Learning + Retrieval-Augmented Generation (RAG) + Vector Search** to deliver:

* Accurate crop predictions
* Contextual explanations
* Similar real-world conditions
* Alternative suggestions

The system is built using a modular architecture and deployed via an interactive **Streamlit web application**.

---

## 🎯 Problem Statement

Farmers and agricultural planners often struggle with selecting the most suitable crop due to:

* Lack of data-driven insights
* Variability in soil nutrients and climate
* Limited access to expert guidance

Traditional ML models only output predictions without explaining **why** a crop is suitable, making them less practical in real-world scenarios.

---

## 💡 Solution

We developed a **Context-Aware AI Crop Advisor** that:

1. Predicts the best crop using a trained ML model
2. Retrieves similar historical conditions using vector search
3. Generates meaningful explanations using contextual data
4. Provides a user-friendly interface for real-time interaction

This system bridges the gap between **prediction and explanation**, making AI more useful and interpretable.

---

## 🧠 Key Features

* ✅ ML-based crop prediction
* ✅ Semantic similarity search (vector-based retrieval)
* ✅ Context-aware explanations (RAG pipeline)
* ✅ Real-time interactive UI using Streamlit
* ✅ Clean and modular code structure

---

## ⚙️ Tech Stack

### 🖥️ Programming & Libraries

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit

### 🤖 Machine Learning

* Random Forest Classifier

### 🔍 Vector Search (Endee Concept)

* Cosine similarity-based retrieval
* Inspired by **Endee Vector Database architecture**

### 🧩 Concepts Used

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Feature Similarity Matching

---

## 🏗️ System Architecture

```
User Input
   ↓
ML Model (Crop Prediction)
   ↓
Vector Search (Similar Conditions)
   ↓
Context Retrieval (JSON + Dataset)
   ↓
Final AI Response (RAG)
   ↓
Streamlit UI Output
```

---

## 🔄 Workflow Explanation

### Step 1: Data Preparation

* Used crop dataset with features:

  * N, P, K
  * Temperature
  * Humidity
  * pH
  * Rainfall

---

### Step 2: Model Training

* Trained a **Random Forest model** to predict crop labels
* Achieved high accuracy due to structured dataset

---

### Step 3: Vector Search Implementation

* Converted dataset into feature vectors
* Used **cosine similarity** to retrieve top-k similar conditions

---

### Step 4: RAG Pipeline

* Combined:

  * ML prediction
  * Retrieved similar data
  * Crop-specific explanations

* Generated a final response including:

  * Recommended crop
  * Reasoning
  * Similar conditions

---

### Step 5: UI Development

* Built using **Streamlit**
* Allows users to:

  * Input soil parameters
  * Get instant AI recommendations

---

## 📊 Example Output

```
🌱 Recommended Crop: Jute

📊 Reason:
Jute grows well with moderate nitrogen, high humidity, and sufficient rainfall.

🔍 Similar Conditions Found:
- Crop: Rice (Temp: 20.8°C, Rainfall: 202mm)
- Crop: Jute (Temp: 23.1°C, Rainfall: 199mm)
- Crop: Jute (Temp: 25.7°C, Rainfall: 191mm)
```

---

## 🚀 How to Run the Project

### 1. Clone Repository

```
git clone <your-repo-link>
cd crop-advisor
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run Application

```
python -m streamlit run app.py
```

---

### 4. Open in Browser

```
http://localhost:8501
```

---

## 📁 Project Structure

```
crop-advisor/
├── data/
│   ├── crop_data.csv
│   ├── crop_info.json
│
├── model/
│   ├── crop_model.pkl
│   ├── train_model.py
│   ├── predict.py
│
├── src/
│   ├── vector_store.py
│   ├── rag_pipeline.py
│
├── app.py
├── test_rag.py
├── requirements.txt
└── README.md
```

---

## 🧩 Endee Integration Note

This project follows the **vector search principles of the Endee database**:

* Data is converted into vector representations
* Similarity-based retrieval is performed
* Used as a core component in the RAG pipeline

Due to local environment constraints, a lightweight cosine similarity-based approach is implemented to simulate vector database behavior.

---

## 🌍 Real-World Applications

* Smart farming advisory systems
* Agri-tech platforms
* Government crop recommendation tools
* Precision agriculture solutions

---

## 🔮 Future Improvements

* Integrate real-time weather APIs
* Add fertilizer recommendations
* Deploy on cloud (AWS/GCP)
* Replace cosine similarity with production-grade vector DB

---

## 👨‍💻 Author

Rajesh Kumar Kinjarapu

---

## 📌 Conclusion

This project demonstrates how modern AI techniques like **RAG and vector search** can transform traditional ML models into **intelligent, explainable systems**, making them more practical for real-world applications.

---
