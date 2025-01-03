# Life Insurance Data Generator

## Overview
The **Insurance Data Generator** is a Python-based tool designed to create synthetic life insurance datasets. This generator simulates realistic policyholder data, which can be used for machine learning, statistical modeling, or testing applications. The generated dataset includes demographic, health, and policy-related information, offering flexibility and customization for various insurance data use cases.

## Features
- Generate synthetic data for 100,000 policyholders (modifiable).
- Includes demographic details (age, gender, income, BMI).
- Simulates health-related data (smoker status, medical history).
- Calculates policy premiums, maximum claims, and policy details.
- Outputs data in tabular format for easy integration into analysis workflows.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/insurance-data-generator.git
   cd insurance-data-generator
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the generator script:
   ```bash
   python src/data_generator.py
The script will generate a Pandas DataFrame containing the insurance data. You can export it as a CSV:
   ```python
   life_insurance_data.to_csv('data/sample_data.csv', index=False)
   ```

## Dataset Columns and Definitions
Below is a detailed description of each column in the generated dataset:
| Column Name            | Description |
| ---------------------- | ----------- |
| policy_id              | Unique identifier for the policy (e.g., pol-123456). |
| inception_date         | The starting date of the policy (format: YYYY-MM-DD). |
| expiry_date            | The ending date of the policy (format: YYYY-MM-DD). |
| tenor_years            | The duration of the policy in years. |
| age                    | Age of the policyholder (between 18 and 80). |
| gender                 | Gender of the policyholder (male or female). |
| annual_income_idr      | Annual income of the policyholder in Indonesian Rupiah (IDR). |
| bmi                    | Body Mass Index (BMI) of the policyholder, calculated as weight (kg) / height² (m²). |
| smoker                 | Indicates whether the policyholder is a smoker (yes or no). |
| medical_history        | Medical history of the policyholder (none, hypertension, diabetes, heart disease, cancer). |
| policy_coverage        | Level of insurance coverage (basic, standard, or comprehensive). |
| total_premium_idr      | Total premium cost of the policy in IDR, calculated based on multiple factors. |
| monthly_premium_idr    | Monthly premium cost in IDR, derived from the total premium divided by the policy's tenor in months. |
| max_claim_amount_idr   | Maximum claimable amount in IDR, based on coverage, health, and income factors. |
| claim_status           | Status of claims for the policy (no claim or claimed). |


## Dataset Example
Here is a snippet of the generated dataset:
| Column Name            | Description |
| ---------------------- | ----------- |
| policy_id              | Unique identifier for the policy (e.g., pol-123456). |
| inception_date         | The starting date of the policy (format: YYYY-MM-DD). |
| expiry_date            | The ending date of the policy (format: YYYY-MM-DD). |
| tenor_years            | The duration of the policy in years. |
| age                    | Age of the policyholder (between 18 and 80). |
| gender                 | Gender of the policyholder (male or female). |
| annual_income_idr      | Annual income of the policyholder in Indonesian Rupiah (IDR). |
| bmi                    | Body Mass Index (BMI) of the policyholder, calculated as weight (kg) / height² (m²). |
| smoker                 | Indicates whether the policyholder is a smoker (yes or no). |
| medical_history        | Medical history of the policyholder (none, hypertension, diabetes, heart disease, cancer). |
| policy_coverage        | Level of insurance coverage (basic, standard, or comprehensive). |
| total_premium_idr      | Total premium cost of the policy in IDR, calculated based on multiple factors. |
| monthly_premium_idr    | Monthly premium cost in IDR, derived from the total premium divided by the policy's tenor in months. |
| max_claim_amount_idr   | Maximum claimable amount in IDR, based on coverage, health, and income factors. |
| claim_status           | Status of claims for the policy (no claim or claimed). |

## Customization
You can modify various constants in the script to generate data that fits your specific needs:

- **Dataset Size**: Adjust the `dataset_size` variable.
- **Age Range**: Modify `min_age` and `max_age`.
- **Income Distribution**: Change `base_income` and `income_std_dev`.
