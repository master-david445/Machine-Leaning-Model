# ENG Basecamp ML Challenge Report

## 1. Project Objective  
The goal of this challenge was to preprocess a dataset with a binary target variable, train five different machine learning models, and evaluate their performance using key metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.  
The deliverables also included generating a confusion matrix, ROC curve, and comparing manual K-Fold cross-validation with `cross_val_score`.

---

## 2. Dataset Description  
- **Dataset Used:** Breast Cancer dataset (`sklearn.datasets.load_breast_cancer`)  
- **Reason for Choice:** Clean, structured, and suitable for binary classification tasks.  
- **Target Variable:** Diagnosis (Malignant = 1, Benign = 0)  
- **Features:** 30 numeric features describing tumor characteristics such as mean radius, texture, and symmetry.

---

## 3. Data Preprocessing  
Steps performed:  
- Loaded dataset and converted to a pandas DataFrame.  
- Checked for missing values and duplicates (none found).  
- Scaled numerical features using `StandardScaler()`.  
- Split data into training (80%) and testing (20%) sets using `train_test_split`.  

Since the dataset was already clean, preprocessing mainly focused on scaling and preparing the data for modeling.

---

## 4. Models Trained  
Five models were trained and compared:

1. Logistic Regression  
2. Decision Tree  
3. Random Forest  
4. K-Nearest Neighbors (KNN)  
5. Support Vector Machine (SVM)

All models were trained using the same train-test split for fair comparison.

---

## 5. Evaluation Metrics  

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|-----------|------------|--------|-----------|----------|
| Logistic Regression | 0.96 | 0.96 | 0.97 | 0.96 | 0.98 |
| Decision Tree | 0.93 | 0.93 | 0.93 | 0.93 | 0.94 |
| Random Forest | 0.97 | 0.97 | 0.97 | 0.97 | 0.99 |
| KNN | 0.95 | 0.95 | 0.95 | 0.95 | 0.96 |
| **SVM** | **0.98** | **0.98** | **0.99** | **0.98** | **1.00** |

---

## 6. Confusion Matrix and ROC Curve  

### Confusion Matrix  
| | Predicted 0 | Predicted 1 |
|--|--|--|
| **Actual 0** | 41 | 2 |
| **Actual 1** | 0 | 71 |

**Interpretation:**  
The model made only two misclassifications, with no false negatives. This means the SVM model correctly classified almost all malignant and benign cases.

### ROC Curve  
- AUC = 1.00  
- The ROC curve stays close to the top-left corner, showing excellent class separation and minimal false positives.

---

## 7. Cross-Validation Comparison  

| Method | Mean Accuracy | Observation |
|--------|----------------|-------------|
| Manual K-Fold (5 splits) | 0.98 | Stable across folds |
| `cross_val_score()` | 0.98 | Similar results confirming consistency |

**Interpretation:**  
Both manual and automatic cross-validation produced almost identical results, confirming the model’s stability and generalization capability.

---

## 8. Best Model and Explanation  

**Best Model:** Support Vector Machine (SVM)

**Reasons for Best Performance:**  
- The dataset has a clear separation between classes.  
- SVM’s margin-maximizing boundary captures this separation effectively.  
- Other models like Decision Tree may overfit, while SVM maintains a strong global decision boundary.  
- Scaling helped improve performance since SVM is sensitive to feature magnitudes.

---

## 9. What I Learned  
- How to preprocess and scale datasets for model training.  
- How to evaluate and compare models using accuracy, precision, recall, and F1-score.  
- How to interpret a confusion matrix and ROC-AUC plot.  
- The concept and implementation of manual vs automated cross-validation.  
- Why SVMs perform well on clean, well-separated data.

---

## 10. Challenges Faced  
- Understanding how to interpret evaluation metrics beyond accuracy.  
- Learning how to correctly implement and compare manual K-Fold and `cross_val_score`.  
- Ensuring proper scaling before fitting models like SVM and KNN.
- interpreting the data generated

---

## 11. Conclusion  
Among the five models trained, the Support Vector Machine (SVM) achieved the highest performance across all metrics, with an AUC of 1.00 and F1-score of 0.98. Its ability to find an optimal separating boundary between classes made it ideal for this dataset.  
This project provided a deeper understanding of preprocessing, model evaluation, and performance interpretation in binary classification problems.