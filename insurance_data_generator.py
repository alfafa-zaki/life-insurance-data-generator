import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Random Seed
np.random.seed(42)

# Parameters
min_age = 18
max_age = 80
base_income = 120000000
income_std_dev = 15000000
young_age_multiplier = 1.8
mid_age_multiplier = 2.2
old_age_multiplier = 1.7
min_young_income = 80000000
min_mid_income = 110000000
bmi_mean = 25
bmi_std_dev = 5
base_premium = 100000
age_premium_factor = 6000
coverage_factors = {'basic': 1.0, 
                    'standard': 1.5, 
                    'comprehensive': 2.0}
smoker_factor = 1.5
gender_factor_male = 1.2
bmi_threshold = 30
bmi_factor = 1.6
medical_history_factors = {'none': 1.0, 
                           'hypertension': 1.2, 
                           'diabetes': 1.3, 
                           'heart disease': 1.5, 
                           'cancer': 2.0}
tenor_premium_multiplier = 8
base_claim = {'basic': 500000000, 
              'standard': 1000000000, 
              'comprehensive': 2000000000}
claim_age_factor = 0.8
claim_smoker_factor = 0.8
claim_gender_factor_male = 0.9
claim_income_divisor = 50000000
claim_tenor_multiplier = 0.1
min_claim_amount = 0.5
max_claim_income_factor = 2.0
min_tenor_years = 1
dataset_size = 100000

min_claim_amount = 50000000
max_claim_difference = 1000000
max_claim_upper_limit = 50000000
report_date_range_min = 30
report_date_range_max = 365
process_date_range_min = 30
process_date_range_max = 90
settlement_date_range_min = 30
settlement_date_range_max = 180
loss_date_range_min = 30
loss_date_range_max = 730
claim_probabilities = [1, 2, 3]
claim_weights = [0.8, 0.15, 0.05]
reinsurer_percentage = 0.2


# Helper Functions
def generate_age():
    return np.random.randint(min_age, max_age)

def generate_gender():
    return random.choice(['male', 'female'])

def generate_income(age):
    base_income_value = np.random.normal(base_income, income_std_dev)
    if age < 30:
        return max(min_young_income, base_income_value * young_age_multiplier)
    elif age < 50:
        return max(min_mid_income, base_income_value * mid_age_multiplier)
    else:
        return max(min_young_income, base_income_value * old_age_multiplier)

def generate_bmi():
    return round(np.random.normal(bmi_mean, bmi_std_dev), 1)

def generate_smoker():
    return random.choice(['yes', 'no'])

def generate_medical_history():
    conditions = ['hypertension', 'diabetes', 'none', 'heart disease', 'cancer']
    return random.choices(conditions, weights=[0.3, 0.2, 0.4, 0.05, 0.05])[0]

def generate_policy_coverage():
    return np.random.choice(['basic', 'standard', 'comprehensive'], p=[0.5, 0.3, 0.2])

def generate_policy_premium(age, coverage, smoker, gender, bmi, medical_history, tenor_years):
    age_factor = (age - min_age) * age_premium_factor
    coverage_factor = coverage_factors[coverage]
    smoker_factor_value = smoker_factor if smoker == 'yes' else 1.0
    gender_factor = gender_factor_male if gender == 'male' else 1.0
    bmi_factor_value = bmi_factor if bmi > bmi_threshold else 1.0
    medical_history_factor = medical_history_factors[medical_history]
    tenor_factor = tenor_years

    return round((base_premium + age_factor * coverage_factor * smoker_factor_value * gender_factor * bmi_factor_value * medical_history_factor) * tenor_factor * tenor_premium_multiplier, -3)

def generate_max_claim(age, coverage, smoker, gender, income, medical_history, tenor_years):
    base_claim_value = base_claim[coverage]
    age_factor = 1.0 if age < 50 else claim_age_factor
    smoker_factor_value = claim_smoker_factor if smoker == 'yes' else 1.0
    gender_factor = 1.0 if gender == 'female' else claim_gender_factor_male
    income_factor = min(max_claim_income_factor, income / claim_income_divisor)
    medical_history_factor = medical_history_factors[medical_history]
    tenor_factor = tenor_years * claim_tenor_multiplier

    return round(base_claim_value * age_factor * smoker_factor_value * gender_factor * income_factor * medical_history_factor * tenor_factor, -6)

def generate_policy_id():
    return f"pol-{np.random.randint(100000, 999999)}"

def generate_inception_date():
    start_date = datetime.now() - timedelta(days=np.random.randint(365, 365 * 5))
    return start_date.replace(month=1, day=1).strftime('%Y-%m-%d')

def generate_expiry_date(inception_date):
    start_date = datetime.strptime(inception_date, '%Y-%m-%d')
    end_year = start_date.year + np.random.randint(min_tenor_years, 6)
    expiry_date = start_date.replace(year=end_year)
    return expiry_date.strftime('%Y-%m-%d')

def calculate_tenor(inception_date, expiry_date):
    start_date = datetime.strptime(inception_date, '%Y-%m-%d')
    end_date = datetime.strptime(expiry_date, '%Y-%m-%d')
    tenor_years = (end_date.year - start_date.year)
    return max(min_tenor_years, tenor_years)

def generate_claim_status():
    return random.choice(['no claim', 'claimed'])

def generate_claim_id(policy_id):
    return f"cl-{policy_id}-{np.random.randint(100000, 999999)}"

def generate_report_date(inception_date):
    start_date = datetime.strptime(inception_date, '%Y-%m-%d')
    report_date = start_date + timedelta(days=np.random.randint(report_date_range_min, report_date_range_max))  # report between 30 days and 1 year
    return report_date.strftime('%Y-%m-%d')

def generate_process_date(report_date):
    report_date_obj = datetime.strptime(report_date, '%Y-%m-%d')
    process_date = report_date_obj + timedelta(days=np.random.randint(process_date_range_min, process_date_range_max))  # processed within 1 to 3 months after report
    return process_date.strftime('%Y-%m-%d')

def generate_settlement_date(process_date):
    process_date_obj = datetime.strptime(process_date, '%Y-%m-%d')
    settlement_date = process_date_obj + timedelta(days=np.random.randint(settlement_date_range_min, settlement_date_range_max))  # settled within 1 to 6 months after process
    return settlement_date.strftime('%Y-%m-%d')

def generate_loss_date(inception_date):
    start_date = datetime.strptime(inception_date, '%Y-%m-%d')
    loss_date = start_date + timedelta(days=np.random.randint(loss_date_range_min, loss_date_range_max))  # loss within 1 to 2 years of inception
    return loss_date.strftime('%Y-%m-%d')

def generate_cause_loss():
    return random.choice(['death', 'accident', 'critical illness', 'natural causes', 'suicide'])

def generate_claim_amount(max_claim):
    max_claim_int = int(max_claim)
    
    # ensure claim amount is smaller than max claim by at least 1 million
    if max_claim_int > max_claim_upper_limit:
        return random.randint(max_claim_upper_limit, max_claim_int - max_claim_difference)
    else:
        return random.randint(max_claim_upper_limit, max_claim_upper_limit)  # return minimum possible claim if max_claim is too low

def generate_claim_reason():
    return random.choice(['damage', 'total loss', 'partial loss', 'health issues', 'natural event'])

def generate_claim_reas_idr(claim_amount):
    return round(claim_amount * reinsurer_percentage, -3)  # reinsurer pays % of the claim amount


# Generate Life Insurance Data Policy Dataset
life_insurance_data = []
for _ in range(dataset_size):
    age = generate_age()
    gender = generate_gender()
    income = generate_income(age)
    bmi = generate_bmi()
    smoker = generate_smoker()
    medical_history = generate_medical_history()
    policy_coverage = generate_policy_coverage()
    policy_id = generate_policy_id()
    inception_date = generate_inception_date()
    expiry_date = generate_expiry_date(inception_date)
    tenor_years = calculate_tenor(inception_date, expiry_date)
    policy_premium = generate_policy_premium(age, policy_coverage, smoker, gender, bmi, medical_history, tenor_years)
    max_claim = generate_max_claim(age, policy_coverage, smoker, gender, income, medical_history, tenor_years)
    monthly_premium = round(policy_premium / (tenor_years * 12), -2)
    claim_status = generate_claim_status()

    life_insurance_data.append({
        'policy_id': policy_id,
        'inception_date': inception_date,
        'expiry_date': expiry_date,
        'tenor_years': tenor_years,
        'age': age,
        'gender': gender,
        'annual_income_idr': income,
        'bmi': bmi,
        'smoker': smoker,
        'medical_history': medical_history,
        'policy_coverage': policy_coverage,
        'total_premium_idr': policy_premium,
        'monthly_premium_idr': monthly_premium,
        'max_claim_amount_idr': max_claim,
        'claim_status': claim_status
    })

life_insurance_data = pd.DataFrame(life_insurance_data)


# Generate Premiums Production Dataset
premium_production = []

for _, row in life_insurance_data.iterrows():
    policy_id = row['policy_id']
    inception_date = datetime.strptime(row['inception_date'], '%Y-%m-%d')
    expiry_date = datetime.strptime(row['expiry_date'], '%Y-%m-%d')
    monthly_premium = row['monthly_premium_idr']
    tenor_years = row['tenor_years']
    
    # transaction dates for each month within the tenure
    current_date = inception_date
    while current_date <= expiry_date and current_date <= datetime.now():
        # transaction_id and transaction_date
        transaction_id = f"{policy_id}-{current_date.strftime('%Y%m%d')}"
        
        # apply discount
        discount = 0
        if random.random() < 0.05:  # % chance for discount
            discount = round(monthly_premium * 0.02, -3)  # A small discount (e.g., 2%)
        
        komisi = round(monthly_premium * 0.05, -3)  # % commission
        premi_reas = round(monthly_premium * 0.10, -3)  # % reinsurance premium
        komisireas = round(premi_reas * 0.15, -3)  # % reinsurance commission
        
        # append the row for each month
        premium_production.append({
            'transaction_id': transaction_id,
            'transaction_date': current_date.strftime('%Y-%m-%d'),
            'policy_id': policy_id,
            'inception_date': row['inception_date'],
            'expiry_date': row['expiry_date'],
            'total_premium_idr': row['total_premium_idr'],
            'gross_premium_idr': monthly_premium,
            'discount': discount,
            'komisi_idr': komisi,
            'premireas_idr': premi_reas,
            'komisireas_idr': komisireas
        })
        
        current_date += timedelta(days=30)  # move to the next month (approximated)

premium_production = pd.DataFrame(premium_production)


# Generate Historical Claim Data
# filter policies with 'claimed' status
claimed_policies = life_insurance_data[life_insurance_data['claim_status'] == 'claimed']

historical_claim_data = []

for _, row in claimed_policies.iterrows():
    policy_id = row['policy_id']
    inception_date = row['inception_date']
    expiry_date = row['expiry_date']
    tenor_years = row['tenor_years']
    max_claim = row['max_claim_amount_idr']
    
    # determine number of claims (propensity for more than 1 claim)
    num_claims = random.choices(claim_probabilities, weights=claim_weights)[0] 
    
    for _ in range(num_claims):
        claim_id = generate_claim_id(policy_id)
        report_date = generate_report_date(inception_date)
        process_date = generate_process_date(report_date)
        settlement_date = generate_settlement_date(process_date)
        loss_date = generate_loss_date(inception_date)
        cause_loss = generate_cause_loss()
        claim_amount = generate_claim_amount(max_claim)
        claim_reason = generate_claim_reason()
        claim_reas_idr = generate_claim_reas_idr(claim_amount)
        
        # append generated claim data to the list
        historical_claim_data.append({
            'claim_id': claim_id,
            'policy_id': policy_id,
            'report_date': report_date,
            'process_date': process_date,
            'settlement_date': settlement_date,
            'date_loss': loss_date,
            'cause_loss': cause_loss,
            'claimamount_idr': claim_amount,
            'claim_reas_idr': claim_reas_idr,
            'inception_date': inception_date,
            'expiry_date': expiry_date,
            'tenor_years': tenor_years,
            'max_claim_amount_idr': max_claim
        })

historical_claim = pd.DataFrame(historical_claim_data)

# Export Data to CSV
life_insurance_data.to_csv('life_insurance_data.csv', index=False)
premium_production.to_csv('premium_production.csv', index=False)
historical_claim_df.to_csv('historical_claim.csv', index=False)
