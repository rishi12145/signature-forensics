# 🖋️ Signature Forensics & Forgery Detection

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=3500&pause=1000&color=3498DB&center=true&vCenter=true&width=700&lines=🖋️+Signature+Forensics+System;🔍+Hybrid+Siamese+Neural+Network;🚀+Real-time+FastAPI+Web+App" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/rishi12145/signature-forensics?style=for-the-badge&color=yellow" alt="stars" />
  <img src="https://img.shields.io/github/forks/rishi12145/signature-forensics?style=for-the-badge&color=blue" alt="forks" />
  <img src="https://img.shields.io/github/license/rishi12145/signature-forensics?style=for-the-badge&color=green" alt="license" />
</p>

---

## 📖 Project Overview

This repository hosts a state-of-the-art **Signature Forensics & Forgery Detection System**. Leveraging a **Hybrid Siamese Network Architecture**, the system blends automated CNN deep-learning representations (EfficientNet-B0) with hand-crafted structural descriptors (HOG & LBP) to accurately assess the authenticity of signatures.

### ⚡ Key Features
* 🧠 **Hybrid Siamese Model:** Uses ResNet/EfficientNet backbones + Handcrafted Feature Extractions (HOG + LBP) fused into unified vector embeddings.
* 🛠️ **Robust Image Processing:** Handles PDF, HEIC, WEBP, PNG, and TIFF formats seamlessly.
* 🖥️ **Interactive Web Interface:** A lightweight, beautifully responsive web dashboard built with **FastAPI** to verify upload queries against reference prototypes.
* ⚡ **Ultra Low Latency:** Employs LRU-cache and memory-mapped dataset pipelines for dynamic model inference.

---

## 🏗️ Architecture & Model Design

```
  User Upload Signature ──►  [Pre-processing & Clean] 
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
┌─────────────────┐                               ┌─────────────────┐
│  EfficientNet   │                               │ Handcrafted Eng │
│  (Deep Vision)  │                               │   (HOG + LBP)   │
└────────┬────────┘                               └────────┬────────┘
         │                                                 │
         ▼                                                 ▼
┌───────────────────────────────────────────────────────────────────┐
│                   Fused Multi-Modal Embeddings                    │
└─────────────────────────────────┬─────────────────────────────────┘
                                  ▼
                    [ Triplet Margin Comparison ]
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
  Distance < Threshold                              Distance > Threshold
    ✅ [VERIFIED REAL]                                ❌ [FORGERY DETECTED]
```

---

## 📂 Repository Structure

```
├── app.py                            # FastAPI Web App Engine & Router
├── signature_verification_pipeline.py# Core Deep Learning Pipeline & Siamese Network
├── signature_forensics.ipynb         # Full Notebook with training steps & experiments
├── templates/
│   └── index.html                    # Responsive frontend layout
├── .gitignore                        # Standard configuration exclusions
└── README.md                         # This Documentation
```

---

## 🚀 Quick Start Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rishi12145/signature-forensics.git
cd signature-forensics
```

### 2️⃣ Install System Dependencies
```bash
pip install -r requirements.txt
```
*Note: Ensure PyMuPDF and PyHeif libraries are properly compiled on your environment for PDF/HEIC support.*

### 3️⃣ Launch the FastAPI Web Server
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🧪 Training & Evaluation Results

* **Primary Loss Metric:** Triplet Margin Loss ($m=0.3$)
* **Best Validation Accuracy:** **95.2%**
* **Area Under ROC Curve (AUC):** **0.978**

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/rishi12145">rishi12145</a>
</p>
