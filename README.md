# 👨‍💻 Software Engineer Salary Prediction

This is a **Machine Learning web application** built with Python and [Streamlit](https://streamlit.io/) that predicts software engineer salaries using data from the **2020 Stack Overflow Developer Survey**.

---

## 🌟 Features

- **📊 Data Exploration**: Visualize salary distribution across different countries, experience levels, and age groups using interactive charts.
- **💰 Salary Prediction**: Estimate your potential salary based on your country, education level, professional experience, and age.
- **🧪 Simple ML Pipeline**: Includes data cleaning, preprocessing, and model training (Linear Regression, Decision Tree, Random Forest).

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system. You will need the following libraries:

- `streamlit`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `numpy`

### Installation

1. Clone or download this repository.
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install streamlit pandas matplotlib scikit-learn numpy
   ```

### Running the App

To start the Streamlit application, run the following command in the project directory:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

- `app.py`: The entry point of the Streamlit application.
- `explore_page.py`: Logic and UI for the data visualization page.
- `predict_page.py`: Logic and UI for the salary prediction page.
- `SalaryPrediction.ipynb`: Jupyter notebook containing the data analysis and model training steps.
- `saved_steps.pkl`: The serialized model and preprocessors (LabelEncoders).
- `survey_results_public.csv`: The dataset from Stack Overflow (ignored by git due to size).

---

## 🛠️ Built With

- **Framework**: [Streamlit](https://streamlit.io/)
- **Data Analysis**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Machine Learning**: [Scikit-learn](https://scikit-learn.org/)
- **Plotting**: [Matplotlib](https://matplotlib.org/)

---

## 📝 Dataset

The data used in this project is sourced from the [2020 Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey). Please note that the CSV file (`survey_results_public.csv`) is excluded from the repository. You can download it directly from Stack Overflow if you wish to retrain the model.

---

*Enjoy predicting! 🚀*
