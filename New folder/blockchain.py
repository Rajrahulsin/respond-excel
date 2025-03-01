import pandas as pd
from faker import Faker
import random

fake = Faker('en_IN')

# Indian first names (40 entries)
first_names = [
    "Aarav", "Riya", "Vikram", "Anjali", "Karan", "Priya", "Rohit", "Sneha", "Raj", "Divya",
    "Arjun", "Meera", "Sanjay", "Pooja", "Rahul", "Neha", "Vivek", "Shreya", "Amit", "Kavita",
    "Aditya", "Anika", "Deepak", "Isha", "Gaurav", "Tanvi", "Nikhil", "Shivani", "Rohan", "Pooja",
    "Siddharth", "Deep", "Ravi", "Mira", "Varun", "Sonia", "Yash", "Preeti", "Akash", "Nandini",
    "Esha", "Shivam", "Gauri", "Harsh", "Ishita", "Jatin", "Kriti", "Lalit", "Mohan", "Naina"
]

# Indian surnames (40 entries, no Khan)
surnames = [
    "Sharma", "Patel", "Singh", "Kumar", "Gupta", "Desai", "Reddy", "Joshi", "Mishra", "Iyer",
    "Chopra", "Malhotra", "Rao", "Verma", "Jain", "Thakur", "Shah", "Mehta", "Bose", "Agarwal",
    "Bhatia", "Choudhury", "Dubey", "Gandhi", "Khanna", "Naidu", "Pandey", "Saxena", "Trivedi", "Yadav",
    "Basu", "Chauhan", "Dutta", "Gill", "Kapoor", "Menon", "Nair", "Rathore", "Sarin", "Tiwari",
    "Bajwa", "Bhasin", "Dharmadhikari", "Gokhale", "Hegde", "Kulkarni", "Mistry", "Rajput", "Seth", "Venkatesan"
]

# Question options (corrected typos)
genders = ["Male", "Female"]
age_ranges = ["15-25", "26-35", "35-40", "40 and above"]
blockchain_familiarity = ["Very familiar", "Somewhat familiar", "Not at all familiar"]
yes_no_maybe = ["Yes", "No", "Maybe"]
scales_5 = [1, 2, 3, 4, 5]
challenges = ["Regulatory barriers", "Lack of understanding/knowledge", "Technology infrastructure", 
              "Data privacy concerns", "Resistance from staff or customers", "Other:"]
payment_challenges = ["High transaction fees", "Slow processing times", "Security vulnerabilities", 
                      "Lack of interoperability", "Other:"]
cybersecurity_risks = ["Hacking and cyberattacks", "Regulatory compliance challenges", 
                       "Data privacy Concerns", "Private key theft or loss"]
financial_constraints = ["High initial costs", "Limited Budget Allocation", 
                         "Uncertain return on investment", "Lack of government incentives"]
banking_areas = ["Payments", "Loans and mortgages", "KYC/AML processes", "Trade finance", 
                 "Cross-border transactions", "Smart contracts", "Other:"]
blockchain_benefits = ["Faster transaction times", "Enhanced security and trust", "Reduced fees", 
                       "Greater accessibility", "Increased transparency", "Other:"]
government_roles = ["Establish clear regulatory frameworks", "Provide financial incentives for blockchain adoption", 
                    "Facilitate collaboration between banks and fintech companies", 
                    "Promote blockchain education and training programs", "Other:"]
strategies = ["Gradual implementation through hybrid models", "Full-scale adoption with dedicated blockchain infrastructure", 
              "Partnering with fintech companies for technical support", 
              "Regulatory driven adoption based on compliance mandates", "Not sure"]

def generate_survey_data(num_responses):
    data = []
    for _ in range(num_responses):
        # Generate Indian name
        name = f"{random.choice(first_names)} {random.choice(surnames)}"
        
        # Randomize answers for all questions
        gender = random.choice(genders)
        age = random.choice(age_ranges)
        familiarity = random.choice(blockchain_familiarity)
        replace_banking = random.choice(yes_no_maybe)
        tech_challenge = random.choice(scales_5)
        challenges_selected = random.sample(challenges, k=random.randint(1, 3))
        payment_issue = random.choice(payment_challenges)
        cybersecurity = random.sample(cybersecurity_risks, k=random.randint(1, 2))
        integration_difficulty = random.choice(scales_5)
        financial_hurdles = random.sample(financial_constraints, k=random.randint(1, 2))
        skill_gap = random.choice(scales_5)
        banking_benefit = random.sample(banking_areas, k=random.randint(1, 3))
        benefits = random.sample(blockchain_benefits, k=random.randint(1, 3))
        financial_inclusion = random.choice(scales_5)
        regulatory_prepared = random.choice(yes_no_maybe)
        gov_role = random.sample(government_roles, k=random.randint(1, 2))
        strategy = random.choice(strategies)
        
        # Append to data
        data.append({
            "Full Name": name,
            "Gender": gender,
            "Age": age,
            "Familiarity with Blockchain": familiarity,
            "Blockchain Replacing Banking?": replace_banking,
            "Technical Challenge Significance (1-5)": tech_challenge,
            "Challenges in Implementing Blockchain": ", ".join(challenges_selected),
            "Biggest Payment Processing Challenge": payment_issue,
            "Cybersecurity Risks": ", ".join(cybersecurity),
            "Difficulty of Integration (1-5)": integration_difficulty,
            "Financial Constraints": ", ".join(financial_hurdles),
            "Lack of Skilled Professionals (1-5)": skill_gap,
            "Banking Areas Benefiting": ", ".join(banking_benefit),
            "Primary Benefits of Blockchain": ", ".join(benefits),
            "Financial Inclusion Likelihood (1-5)": financial_inclusion,
            "Regulatory Preparedness": regulatory_prepared,
            "Government’s Role": ", ".join(gov_role),
            "Most Effective Strategy": strategy
        })
    return pd.DataFrame(data)

# Generate 200 responses and save to Excel
df = generate_survey_data(200)
df.to_excel("Banking_Blockchain_Survey_Responses.xlsx", index=False)