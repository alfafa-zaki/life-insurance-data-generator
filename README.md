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
   git clone https://github.com/alfafa-zaki/life-insurance-data-generator.git
   cd life-insurance-data-generator
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the generator script:
   ```bash
   python insurance_data_generator.py
   ```
   The script will generate a Pandas DataFrame containing the insurance data. You can export it as a CSV:
   ```python
   life_insurance_data.to_csv('life_insurance_data.csv', index=False)
   premium_production.to_csv('premium_production.csv', index=False)
   historical_claim.to_csv('historical_claim.csv', index=False)
   ```

## Dataset Columns and Definitions
Below is a detailed description of each column in the generated dataset:
| Column Name             | Description                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------|
| policy_id               | Unique identifier for the insurance policy.                                                          |
| inception_date          | The date when the policy started or was issued.                                                      |
| expiry_date             | The date when the policy ends or expires.                                                            |
| tenor_years             | The duration of the policy in years.                                                                  |
| age                     | The age of the policyholder at the time of the policy issuance.                                      |
| gender                  | The gender of the policyholder (e.g., Male, Female).                                                 |
| annual_income_idr       | The annual income of the policyholder in Indonesian Rupiah (IDR).                                    |
| bmi                     | The Body Mass Index (BMI) of the policyholder, a measure of body fat based on height and weight.     |
| smoker                  | Whether the policyholder is a smoker (Yes or No).                                                    |
| medical_history         | Any relevant medical conditions or history of the policyholder (e.g., hypertension, diabetes).       |
| policy_coverage         | The type of coverage provided by the insurance policy (e.g., life, health, critical illness).         |
| total_premium_idr       | The total premium amount of the insurance policy in Indonesian Rupiah (IDR).                         |
| monthly_premium_idr     | The amount the policyholder pays monthly as the premium in Indonesian Rupiah (IDR).                   |
| max_claim_amount_idr    | The maximum amount the policyholder can claim under the policy, in Indonesian Rupiah (IDR).          |
| claim_status            | The status of the claim (e.g., Pending, Approved, Rejected).                                         |
| transaction_id          | Unique identifier for the transaction related to the policy.                                         |
| transaction_date        | The date the transaction occurred (e.g., payment or update).                                          |
| gross_premium_idr       | The total premium amount before any deductions, in Indonesian Rupiah (IDR).                          |
| discount                | Any discounts applied to the premium amount.                                                         |
| komisi_idr              | The commission earned by the agent or intermediary, in Indonesian Rupiah (IDR).                      |
| premi_reas_idr          | The portion of the premium amount that is reinsured, in Indonesian Rupiah (IDR).                     |
| komisireas_idr          | The commission paid by the reinsurer, in Indonesian Rupiah (IDR).                                     |
| claim_id                | Unique identifier for the insurance claim.                                                           |
| report_date             | The date when the claim report was created.                                                          |
| process_date            | The date when the claim was processed.                                                               |
| settlement_date         | The date when the claim settlement was made or paid out.                                             |
| date_loss                | The date when the loss or event leading to the claim occurred.                                        |
| cause_loss              | The reason for the claim (e.g., Death, Accident, Critical Illness).                                  |
| claimamount_idr         | The total claim amount in Indonesian Rupiah (IDR).                                                   |
| claim_reas_idr          | The reinsurer’s portion of the claim amount, in Indonesian Rupiah (IDR).                             |

## Dataset Example
Here is a snippet of the generated dataset:
| policy_id  | inception_date | expiry_date | tenor_years | age | gender | annual_income_idr | bmi  | smoker | medical_history | policy_coverage | total_premium_idr | monthly_premium_idr | max_claim_amount_idr | claim_status |
| ---------- | -------------- | ----------- | ----------- | --- | ------ | ----------------- | ---- | ------ | ---------------- | ---------------- | ------------------ | -------------------- | --------------------- | ------------ |
| pol-123456 | 2020-01-01     | 2025-01-01  | 5           | 45  | male   | 150,000,000       | 27.5 | no     | none             | comprehensive    | 12,000,000         | 200,000              | 1,500,000,000         | claimed      |
| pol-654321 | 2019-01-01     | 2024-01-01  | 5           | 30  | female | 120,000,000       | 22.4 | yes    | hypertension     | standard         | 9,600,000          | 160,000              | 800,000,000           | no claim    |

## Customization
You can modify various constants in the script to generate data that fits your specific needs:

- **Dataset Size**: Adjust the `dataset_size` variable.
- **Age Range**: Modify `min_age` and `max_age`.
- **Income Distribution**: Change `base_income` and `income_std_dev`.
