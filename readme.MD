# 🏥 Healthcare Billing Prediction Model

A machine learning model to predict hospital billing amounts based on patient characteristics. Deployed as an interactive web application using Streamlit.

## Features

- **Accurate Predictions**: Uses Linear Regression trained on healthcare data
- **User-Friendly Interface**: Interactive Streamlit web application
- **Real-time Predictions**: Get billing estimates instantly
- **Easy to Use**: Simple form-based input for patient information

## Model Details

- **Algorithm**: Linear Regression
- **Input Features**: 
  - Age
  - Gender
  - Length of Stay
  - Medical Condition
  - Service Type
- **Target**: Billed Amount (₹)

## Project Structure

```
healthcare-billing-predictor/
├── app.py                              # Main Streamlit application
├── train_model.py                      # Model training script
├── requirements.txt                    # Python dependencies
├── simple_healthcare_model.pkl         # Trained model (generated)
├── .gitignore                          # Git ignore file
└── README.md                           # This file
```

## Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/healthcare-billing-predictor.git
   cd healthcare-billing-predictor
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

## Model Training

If you want to retrain the model with your own data:

1. **Prepare your data**: Ensure your Excel file contains columns:
   - `age`
   - `gender`
   - `length_of_stay_days`
   - `medical_condition`
   - `service_type`
   - `billed_amount_inr`

2. **Update the data path** in `train_model.py`

3. **Run the training script**
   ```bash
   python train_model.py
   ```

4. **New model** will be saved as `simple_healthcare_model.pkl`

## Deployment on Streamlit Cloud

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at https://streamlit.io/cloud)

### Step-by-Step Deployment

1. **Ensure all files are in your GitHub repository** (checked in the next section)

2. **Go to Streamlit Cloud**
   - Visit https://share.streamlit.io/
   - Sign in with your GitHub account

3. **Create new app**
   - Click "Create app" button
   - Select your repository
   - Select the branch (usually `main`)
   - Set main file path to `app.py`
   - Click "Deploy"

4. **Your app is live!**
   - Streamlit will automatically build and deploy
   - You'll get a shareable URL like: `https://your-app-name.streamlit.app/`

## GitHub Setup

### Create Repository on GitHub

1. **Go to github.com** and click "New repository"

2. **Repository settings**
   - Name: `healthcare-billing-predictor`
   - Description: "Healthcare Billing Amount Prediction Model"
   - Visibility: Public
   - Click "Create repository"

3. **Push code to GitHub** (from your local machine)
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Healthcare billing prediction model"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/healthcare-billing-predictor.git
   git push -u origin main
   ```

## File Checklist Before Deployment

- ✅ `app.py` - Streamlit application
- ✅ `simple_healthcare_model.pkl` - Trained model file
- ✅ `requirements.txt` - Python dependencies
- ✅ `README.md` - Documentation
- ✅ `.gitignore` - Git ignore rules

## Usage Example

1. Open the deployed app
2. Fill in patient information:
   - Age: 45
   - Gender: Male
   - Length of Stay: 3 days
   - Medical Condition: Diabetes
   - Service Type: Surgery
3. Click "Predict Billing Amount"
4. Get your estimated billing amount

## Important Notes

⚠️ **Disclaimer**: This tool provides estimates based on historical data. Actual billing may vary based on:
- Specific hospital policies
- Additional procedures
- Insurance coverage
- Regional variations
- Emergency charges

## Dependencies

- **streamlit** - Web application framework
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning
- **joblib** - Model serialization
- **openpyxl** - Excel file handling

See `requirements.txt` for versions.

## Performance Metrics

Based on the training data:
- **Mean Absolute Error (MAE)**: Indicates average prediction error
- **Root Mean Squared Error (RMSE)**: Shows spread of errors
- **R² Score**: Indicates model fit quality

These metrics help evaluate model accuracy.

## Future Improvements

- [ ] Add data visualization/charts
- [ ] Include confidence intervals
- [ ] Integrate with hospital databases
- [ ] Add more features (comorbidities, procedures)
- [ ] Deploy with advanced models (XGBoost, Neural Networks)
- [ ] Add multilingual support

## Troubleshooting

### Model file not found error
- Ensure `simple_healthcare_model.pkl` is in the root directory
- The model is generated when you run `train_model.py`

### Missing columns error
- Verify the feature columns match the training data
- Check for spelling errors in medical condition and service type

### Streamlit app won't load
- Check all dependencies in `requirements.txt` are installed
- Run `pip install -r requirements.txt` again

## License

This project is open source and available under the MIT License.

## Contact & Support

For questions or issues:
- Open an issue on GitHub
- Check Streamlit documentation: https://docs.streamlit.io/

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Machine Learning with [Scikit-learn](https://scikit-learn.org/)
- Data processing with [Pandas](https://pandas.pydata.org/)

---

**Made with ❤️ for healthcare data prediction**