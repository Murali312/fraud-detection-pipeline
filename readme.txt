# 🚀 Fraud Detection Pipeline (Pandas + NumPy)

## 📌 Project Overview

This project is an **end-to-end data preprocessing and feature engineering pipeline** designed for **fraud detection in financial transactions**.

It simulates a **real-world Machine Learning workflow** where raw transaction data is:

1. Ingested
2. Cleaned
3. Transformed into meaningful features
4. Saved as model-ready dataset

---

## 🎯 Objective

To build a **production-like data pipeline** using:

* **Pandas** → Data manipulation & cleaning
* **NumPy** → Fast numerical operations
* **Python** → Modular pipeline design

This pipeline prepares data for **fraud detection ML models** like:

* Logistic Regression
* Random Forest
* XGBoost

---

## 🧱 Project Structure

```
fraud-detection-pipeline/
│
├── data/
│   ├── raw/
│   │   └── transactions.csv
│   ├── processed/
│   └── features/
│       └── feature_data.csv
│
├── src/
│   ├── ingestion.py
│   ├── cleaning.py
│   ├── feature_engineering.py
│   ├── pipeline.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Description

File: `data/raw/transactions.csv`

| Column         | Description                             |
| -------------- | --------------------------------------- |
| transaction_id | Unique transaction ID                   |
| user_id        | User identifier                         |
| amount         | Transaction amount                      |
| time           | Timestamp                               |
| merchant       | Merchant name                           |
| location       | Transaction location                    |
| is_fraud       | Target variable (0 = normal, 1 = fraud) |

---

## ⚙️ Pipeline Workflow

### 1️⃣ Data Ingestion

* Reads CSV file using Pandas

### 2️⃣ Data Cleaning

* Convert time to datetime
* Handle missing values
* Remove duplicates

### 3️⃣ Feature Engineering 🔥

Created features:

* `txn_count` → Number of transactions per user
* `avg_amount` → Average transaction amount per user
* `time_diff` → Time gap between transactions
* `high_amount` → Flag for large transactions
* `foreign_txn` → Flag for foreign transactions

### 4️⃣ Save Output

* Stores processed data in `data/features/feature_data.csv`

---

## 🧠 Key Concepts Used

* Pandas:

  * `read_csv()`, `to_csv()`
  * `groupby()`, `transform()`
  * `fillna()`, `drop_duplicates()`

* NumPy:

  * `np.where()` (vectorization)
  * Statistical operations

---

## ▶️ How to Run the Project

### 🔹 Step 1: Clone Repository

```bash
git clone <your-repo-url>
cd fraud-detection-pipeline
```

---

### 🔹 Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 4: Add Dataset

Create file:

```
data/raw/transactions.csv
```

Add sample data:

```
transaction_id,user_id,amount,time,merchant,location,is_fraud
1,101,500,2024-01-01 10:00:00,Amazon,India,0
2,102,20000,2024-01-01 10:05:00,Flipkart,India,1
3,101,300,2024-01-01 11:00:00,Amazon,India,0
4,103,15000,2024-01-01 11:10:00,Unknown,USA,1
5,101,700,2024-01-01 12:00:00,Amazon,India,0
```

---

### 🔹 Step 5: Run Pipeline

```bash
python src/main.py
```

---

## 📈 Output

Generated file:

```
data/features/feature_data.csv
```

Sample Output:

| user_id | amount | txn_count | avg_amount | time_diff | high_amount | foreign_txn | is_fraud |
| ------- | ------ | --------- | ---------- | --------- | ----------- | ----------- | -------- |
| 101     | 500    | 3         | 500        | 0         | 0           | 0           | 0        |

---

## ⚠️ Common Errors & Fixes

### ❌ File Not Found

✔ Ensure correct file path
✔ Run from project root

---

### ❌ Directory Not Found

✔ Create folder manually OR
✔ Use:

```python
os.makedirs(path, exist_ok=True)
```

---

## 🤖 How This Helps in AI/ML

This pipeline produces **model-ready features**:

```python
X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]
```

Used in:

* Fraud detection systems
* Banking risk analysis
* Real-time anomaly detection

---

## 🚀 Future Improvements

* Add model training (Scikit-learn)
* Add logging system
* Convert to API (FastAPI)
* Integrate with frontend dashboard
* Deploy as ML service

---

## 💡 Why This Project Matters

This is not just a script — it demonstrates:

✅ Real-world data pipeline design
✅ Feature engineering skills
✅ Production-level thinking
✅ ML readiness

---

## 👨‍💻 Author

**Murali C**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and keep building 🚀
