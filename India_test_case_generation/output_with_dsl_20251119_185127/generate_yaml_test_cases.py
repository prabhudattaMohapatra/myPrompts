import csv
import yaml
from decimal import Decimal

# Read test case mapping
def get_test_case_mappings():
    """Get employee to test case mappings"""
    return {
        'EMP001': 'TC-01',
        'EMP002': 'TC-02',
        'EMP003': 'TC-03',
        'EMP004': 'TC-04',
        'EMP005': 'TC-05',
        'EMP006': 'TC-06',  # Already generated
        'EMP007': 'TC-07',
        'EMP008': 'TC-08',
        'EMP009': 'TC-09',
        'EMP010': 'TC-10',
        'EMP011': 'TC-11',
        'EMP012': 'TC-12',
        'EMP013': 'TC-13',
        'EMP014': 'TC-14',
        'EMP015': 'TC-15',
        'EMP016': 'TC-16',
        'EMP017': 'TC-17',
        'EMP018': 'TC-18',
        'EMP019': 'TC-19',
        'EMP020': 'TC-20',
        'EMP021': 'TC-21',
        'EMP022': 'TC-23',  # No TC-22
        'EMP023': 'TC-24',
        'EMP024': 'TC-25',
        'EMP025': 'TC-26',
        'EMP026': 'TC-27',
        'EMP027': 'TC-28',
        'EMP028': 'TC-29',
        'EMP029': 'TC-30',
        'EMP030': 'TC-31',
    }

def get_test_case_descriptions():
    """Get test case descriptions"""
    return {
        'TC-01': ('NewRegimeBelowExemption', 'New Regime - Below Exemption Limit'),
        'TC-02': ('NewRegimeRebateThreshold', 'New Regime - Rebate Threshold Boundary'),
        'TC-03': ('NewRegimeMarginalRelief', 'New Regime - Marginal Relief Zone'),
        'TC-04': ('NewRegimeHighIncomeSurcharge', 'New Regime - High Income with Surcharge'),
        'TC-05': ('NewRegimeMultipleExemptions', 'New Regime - Multiple Deduction and Exemption'),
        'TC-06': ('OldRegimeMultipleDeductions', 'Old Regime - Multiple Deductions'),
        'TC-07': ('OldRegimeSeniorCitizen', 'Old Regime - Senior Citizen (60-80)'),
        'TC-08': ('OldVsNewComparison', 'Old vs New - Regime Comparison Case'),
        'TC-09': ('VeryHighIncomeMaxSurcharge', 'Very High Income - Maximum Surcharge'),
        'TC-10': ('HRAMetroMaxExemption', 'HRA - Metro City Maximum Exemption'),
        'TC-11': ('HRANonMetroMinimal', 'HRA - Non-Metro with Minimal Exemption'),
        'TC-12': ('Section80GGNoHRA', 'Section 80GG - No HRA Received'),
        'TC-13': ('MultipleAllowancesCombined', 'Multiple Allowances Combined'),
        'TC-14': ('MaxDeductionsOldRegime', 'Maximum Deductions Scenario (Old Regime)'),
        'TC-15': ('NPSEmployeeEmployer', 'NPS - Both Employee & Employer Contributions'),
        'TC-16': ('HomeLoanMultipleProperties', 'Home Loan - Multiple Properties'),
        'TC-17': ('DisabilityBenefits', 'Disability & Dependent Benefits'),
        'TC-18': ('InvestmentDonationCombined', 'Investment & Donation Combinations'),
        'TC-19': ('ULIPCapitalGains', 'ULIP & Capital Gains'),
        'TC-20': ('Gratuity Section89Relief', 'Gratuity with Section 89 Relief (15+ years)'),
        'TC-21': ('EPFWithdrawalBefore5Years', 'EPF Withdrawal Before 5 Years'),
        'TC-23': ('NRIEmployee', 'NRI Employee'),
        'TC-24': ('MultipleEmployersSameYear', 'Multiple Employers in Same Year'),
        'TC-25': ('MidYearSalaryChange', 'Mid-Year Salary Structure Change'),
        'TC-26': ('ProfessionalTaxMultipleStates', 'Professional Tax - Multiple States'),
        'TC-27': ('TDSThresholdRentPayment', 'TDS Threshold Testing - Rent Payment'),
        'TC-28': ('VPFContributionLowIncome', 'VPF Contribution (Low Income)'),
        'TC-29': ('AdditionalRentalIncome', 'Additional Income (Rental)'),
        'TC-30': ('MidYearRegimeChange', 'Mid-Year Tax Regime Change'),
        'TC-31': ('MonthlyInvestmentUpdate', 'Monthly Investment Update (Old Regime)'),
    }

def generate_yaml_test_case(emp_input, emp_output, test_case_id):
    """Generate a single YAML test case file"""
    
    tc_info = get_test_case_descriptions().get(test_case_id, ('Unknown', 'Unknown Test Case'))
    scenario_name, description = tc_info
    
    # Build rules applied list based on regime and components
    rules_applied = [
        f"IN-IT-SLAB-{emp_input['tax_regime'].upper()}-2025-001",
        f"IN-87A-2025-REB-{'002' if emp_input['tax_regime'] == 'new' else '001'}",
        f"IN-STD-2025-DED-{'002' if emp_input['tax_regime'] == 'new' else '001'}",
        "IN-SAL-2025-COMP-001",
        "IN-SAL-2025-COMP-002",
        "IN-TAX-2025-CALC-001",
        f"IN-TAX-2025-SLAB-{'004' if emp_input['tax_regime'] == 'new' else '002'}",
        "IN-CESS-2025-CALC-001",
        "IN-NET-2025-CALC-001"
    ]
    
    # Add specific rules based on components
    if float(emp_output.get('hra_exemption', 0)) > 0:
        rules_applied.append("IN-HRA-2025-EXE-001")
    if float(emp_output.get('conveyance_exemption', 0)) > 0:
        rules_applied.append("IN-CON-2025-EXE-001")
    if float(emp_output.get('lta_exemption', 0)) > 0:
        rules_applied.append("IN-LTA-2025-EXE-001")
    if float(emp_output.get('80c_deduction', 0)) > 0:
        rules_applied.append("IN-80C-2025-DED-001")
    if float(emp_output.get('80d_total_deduction', 0)) > 0:
        rules_applied.append("IN-80D-2025-DED-001")
    if float(emp_output.get('80g_deduction', 0)) > 0:
        rules_applied.append("IN-80G-2025-DED-001")
    if float(emp_output.get('surcharge', 0)) > 0:
        rules_applied.append("IN-SURCHARGE-2025-001")
    
    # Build YAML structure
    yaml_data = {
        'metadata': {
            'type': 'test_case',
            'version': '2025-26',
            'jurisdiction': 'IN',
            'effective_date': '2025-04-01',
            'description': f'Test Case {test_case_id}: {description}',
            'test_case_id': test_case_id,
            'scenario_name': scenario_name,
            'assessment_year': '2025-26'
        },
        'rules_applied': rules_applied,
        'employee_profile': {
            'personal_details': {
                'employee_id': emp_input['employee_id'],
                'first_name': emp_input.get('first_name', ''),
                'last_name': emp_input.get('last_name', ''),
                'age': int(emp_input.get('age', 0)),
                'date_of_birth': emp_input.get('date_of_birth', ''),
                'gender': emp_input.get('gender', ''),
                'pan': emp_input.get('pan', '')
            },
            'location': {
                'state': emp_input.get('state', ''),
                'city': emp_input.get('city', ''),
                'city_type': emp_input.get('city_type', ''),
                'residency': emp_input.get('residency', 'IN')
            },
            'employment_details': {
                'employment_type': emp_input.get('employment_type', ''),
                'employment_status': emp_input.get('employment_status', ''),
                'employer_type': emp_input.get('employer_type', ''),
                'date_of_joining': emp_input.get('date_of_joining', ''),
                'service_years': float(emp_input.get('service_years', 0))
            },
            'tax_regime': emp_input['tax_regime']
        },
        'income_components': {
            'salary': {
                'annual_ctc': float(emp_input.get('annual_ctc', 0)),
                'gross_salary': float(emp_input.get('gross_salary', 0)),
                'basic_salary': float(emp_input.get('basic_salary', 0)),
                'hra_received': float(emp_input.get('hra_received', 0)),
                'special_allowance': float(emp_input.get('special_allowance', 0)),
                'conveyance_allowance': float(emp_input.get('conveyance_allowance', 0)),
                'transport_allowance': float(emp_input.get('transport_allowance', 0)),
                'lta_received': float(emp_input.get('lta_received', 0)),
                'meal_vouchers': float(emp_input.get('meal_vouchers', 0))
            },
            'bonuses': {
                'annual_bonus': float(emp_input.get('bonus', 0)),
                'commission': float(emp_input.get('commission', 0))
            },
            'deductions': {
                'employee_pf_contribution': float(emp_input.get('employee_pf_contribution', 0)),
                'employer_pf_contribution': float(emp_input.get('employer_pf_contribution', 0)),
                'professional_tax_paid': float(emp_input.get('professional_tax_paid', 0))
            },
            'investments_declarations': {
                'section_80c_investments': float(emp_input.get('section_80c_investments', 0)),
                'nps_employee_contribution': float(emp_input.get('nps_employee_contribution', 0)),
                'nps_employer_contribution': float(emp_input.get('nps_employer_contribution', 0)),
                'nps_additional_contribution': float(emp_input.get('nps_additional_contribution', 0)),
                'health_insurance_premium': float(emp_input.get('self_family_premium', 0)) + float(emp_input.get('parents_premium', 0))
            }
        },
        'expected_results': {
            'gross_total_income_calculation': {
                'total_gross_income': float(emp_output.get('gross_income', 0))
            },
            'exemptions': {
                'hra_exemption': float(emp_output.get('hra_exemption', 0)),
                'conveyance_exemption': float(emp_output.get('conveyance_exemption', 0)),
                'lta_exemption': float(emp_output.get('lta_exemption', 0)),
                'transport_exemption': float(emp_output.get('transport_exemption', 0)),
                'total_exemptions': float(emp_output.get('total_exemptions', 0))
            },
            'deductions': {
                'standard_deduction': float(emp_output.get('standard_deduction', 0)),
                'professional_tax': float(emp_output.get('professional_tax_deduction', 0)),
                '80c_deduction': float(emp_output.get('80c_deduction', 0)),
                '80d_deduction': float(emp_output.get('80d_total_deduction', 0)),
                '80g_deduction': float(emp_output.get('80g_deduction', 0)),
                'total_deductions': float(emp_output.get('total_deductions', 0))
            },
            'taxable_income_calculation': {
                'gross_income': float(emp_output.get('gross_income', 0)),
                'total_exemptions': float(emp_output.get('total_exemptions', 0)),
                'total_deductions': float(emp_output.get('total_deductions', 0)),
                'taxable_income': float(emp_output.get('taxable_income', 0))
            },
            'tax_calculation': {
                'base_tax': float(emp_output.get('base_tax', 0)),
                'rebate_87a': float(emp_output.get('rebate_87a', 0)),
                'tax_after_rebate': float(emp_output.get('tax_after_rebate', 0)),
                'surcharge': float(emp_output.get('surcharge', 0)),
                'tax_with_surcharge': float(emp_output.get('tax_with_surcharge', 0)),
                'health_education_cess': float(emp_output.get('health_education_cess', 0)),
                'total_tax_liability': float(emp_output.get('total_tax_liability', 0))
            },
            'monthly_tds': float(emp_output.get('monthly_tds', 0)),
            'net_salary': float(emp_output.get('net_salary', 0))
        }
    }
    
    return yaml_data

def main():
    """Main function to generate all YAML test cases"""
    
    # Load input and output data
    print("Loading employee data...")
    input_data = {}
    with open('annual_employee_input_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            input_data[row['employee_id']] = row
    
    output_data = {}
    with open('annual_tax_forecast.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            output_data[row['employee_id']] = row
    
    # Get mappings
    mappings = get_test_case_mappings()
    
    # Already generated test cases
    already_generated = ['TC-01', 'TC-06']
    
    # Generate YAML files
    count = 0
    for emp_id, tc_id in mappings.items():
        if tc_id in already_generated:
            print(f"⏭️  Skipping {tc_id} (already generated)")
            continue
        
        if emp_id not in input_data or emp_id not in output_data:
            print(f"⚠️  Warning: Missing data for {emp_id} ({tc_id})")
            continue
        
        emp_input = input_data[emp_id]
        emp_output = output_data[emp_id]
        
        tc_info = get_test_case_descriptions().get(tc_id, ('Unknown', 'Unknown Test Case'))
        scenario_name, description = tc_info
        
        yaml_data = generate_yaml_test_case(emp_input, emp_output, tc_id)
        
        filename = f"{tc_id}_{scenario_name}.yaml"
        with open(filename, 'w') as f:
            yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        count += 1
        print(f"✓ Generated {filename}")
    
    print(f"\\n✅ Generated {count} YAML test case files!")

if __name__ == '__main__':
    main()
