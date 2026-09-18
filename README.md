\# Olist E-Commerce Review Risk Prediction
[🚀 Live Demo](https://olist-ecommerce-review-risk-prediction.streamlit.app) | [📂 GitHub Repository](https://github.com/mohammedmustafa678/olist-ecommerce-review-risk-prediction)



An end-to-end machine learning project using the Brazilian Olist e-commerce dataset to predict whether an order is likely to receive a bad customer review.



The project combines data cleaning, exploratory data analysis, feature engineering, machine learning model comparison, threshold optimization, and a Streamlit prediction application.



\---



\## Project Overview



Customer reviews are an important indicator of e-commerce customer experience.



This project investigates whether information available \*\*at the time an order is placed\*\* can be used to identify orders that are more likely to receive a low review score.



The goal is not to predict the exact review score, but to classify orders into:



Low Risk — less likely to receive a bad review

High Risk — more likely to receive a bad review



This can potentially help an e-commerce business identify higher-risk orders and prioritize proactive customer-service interventions.



\---



\## Business Problem



An e-commerce company receives thousands of orders and cannot manually monitor every customer experience.



A predictive model could help answer:



> \*\*Which orders are more likely to result in a bad customer review?\*\*



The model is designed around information that would realistically be available when the order is placed.



This means the model intentionally excludes information that becomes available only after delivery, such as:



\- Actual delivery time

\- Delivery delay

\- Review score

\- Review information

\- Post-purchase order outcomes



This helps reduce data leakage and makes the prediction scenario more realistic.



\---



\## Dataset



The project uses the \*\*Olist Brazilian E-Commerce Public Dataset\*\*.



The dataset contains information about:



\- Customers

\- Orders

\- Products

\- Sellers

\- Order items

\- Payments

\- Reviews

\- Product categories

\- Customer locations



The original dataset contains approximately 100,000 orders.



The geolocation dataset was used during analysis but is excluded from this repository because of its large file size.



\---



\## Data Preparation



The datasets were inspected for:



\- Missing values

\- Duplicate records

\- Invalid relationships between tables

\- Date formats

\- Zero or invalid product measurements

\- Review duplication

\- Order-level aggregation



Exact duplicate records were removed from the geolocation dataset during analysis.



Date columns were converted to proper datetime format.



Product weights containing zero values were treated as missing values rather than valid measurements.



Reviews were aggregated at the order level before being merged into the main analytical dataset.



\---



\## Feature Engineering



An order-level analytical dataset was created by combining information from multiple Olist tables.



Examples of engineered features include:



\### Order and Product Features



\- Number of items

\- Total product price

\- Total freight cost

\- Total order value



\### Payment Features



\- Number of payment records

\- Total payment value

\- Maximum number of installments



\### Delivery Planning



\- Estimated delivery duration



\### Customer Information



\- Customer state



\### Purchase Timing



\- Purchase month

\- Day of week

\- Purchase hour



\---



\## Target Variable



The target variable is:



`bad\_review`



An order is classified as a bad-review order when its aggregated mean review score is less than or equal to 2.



Orders without a review were excluded from the modeling dataset.



Final modeling dataset:



\- \*\*98,673 orders\*\*

\- \*\*25 columns before model feature preparation\*\*



Target distribution:



\- Good review: \*\*84,224\*\*

\- Bad review: \*\*14,449\*\*



The target is therefore imbalanced, making accuracy alone an unsuitable metric for evaluating the model.



\---



\## Exploratory Data Analysis



Several patterns were identified during analysis.



\### Delivery and Reviews



Late delivery showed a strong association with lower review scores.



Among delivered orders:



\- 96,476 orders had a calculated delivery duration

\- 6,535 were delivered after the estimated delivery date

\- Late delivery rate: approximately \*\*6.77%\*\*



Average review score:



| Delivery Status | Mean Review Score |

|---|---:|

| Not late | 4.29 |

| Late | 2.27 |



This is an observational relationship and should not be interpreted as proof that late delivery directly causes low reviews.



\---



\### Customer Repeat Behavior



The majority of customers placed only one order.



Approximately \*\*96.9%\*\* of customers were one-time customers, while approximately \*\*3.1%\*\* placed multiple orders.



Repeat customers had higher total lifetime spending in the dataset, although this naturally reflects their larger number of orders and should not be interpreted as a higher average order value.



\---



\### Review Distribution



The review scores were heavily concentrated around 5 stars.



| Review Score | Orders |

|---|---:|

| 1 | 11,424 |

| 2 | 3,151 |

| 3 | 8,179 |

| 4 | 19,142 |

| 5 | 57,328 |



Approximately \*\*14.7%\*\* of reviewed orders were classified as bad reviews.



\---



\## Machine Learning



Multiple classification algorithms were benchmarked using stratified cross-validation.



Models evaluated included:



\- Logistic Regression

\- Ridge Classifier

\- SGD Classifier

\- Perceptron

\- Passive Aggressive

\- K-Nearest Neighbors

\- Decision Tree

\- Random Forest

\- Extra Trees

\- AdaBoost

\- Gradient Boosting

\- HistGradientBoosting

\- Gaussian Naive Bayes

\- Bernoulli Naive Bayes

\- Linear SVC

\- Linear Discriminant Analysis

\- Quadratic Discriminant Analysis

\- XGBoost

\- LightGBM

\- CatBoost



Because the target was imbalanced, model selection focused primarily on \*\*F1-score\*\*, while also considering precision, recall, and ROC-AUC.



\---



\## Model Selection



The final model selected was:



\*\*HistGradientBoostingClassifier\*\*



The decision threshold was optimized using cross-validation rather than tuning directly on the final test set.



Selected classification threshold:



\*\*0.17\*\*



The final model was then evaluated once on the untouched test set.



\### Final Test Performance



| Metric | Score |

|---|---:|

| Accuracy | 75.43% |

| Precision | 27.06% |

| Recall | 39.97% |

| F1 Score | 32.27% |

| ROC-AUC | 64.85% |



The relatively low precision means the model will generate a number of false positives.



Therefore, the model is better viewed as a \*\*risk-ranking and customer-experience intervention tool\*\* rather than a definitive prediction system.



\---



\## Confusion Matrix



Final test-set confusion matrix at the selected threshold:



```text

[13732  3113]

[01735  1155]]

