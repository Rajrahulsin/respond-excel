# Banking Blockchain Survey Data Generator

A Python script that generates synthetic survey data about blockchain adoption in the banking sector, specifically focused on the Indian context.

## Description

This tool creates realistic mock survey responses about blockchain technology adoption in banking, using Indian names and various relevant parameters. It generates structured data that can be used for analysis, testing, or demonstration purposes.

## Features

- Generates synthetic survey responses with Indian names
- Creates realistic demographic and opinion data
- Covers multiple aspects of blockchain adoption:
  - Technical challenges
  - Payment processing
  - Cybersecurity risks
  - Financial constraints
  - Banking applications
  - Regulatory aspects
  - Implementation strategies

## Requirements

- Python 3.x
- pandas
- Faker

## Installation

```bash
pip install pandas faker
```

## Usage

```python
from blockchain import generate_survey_data

# Generate 200 survey responses
df = generate_survey_data(200)

# Save to Excel file
df.to_excel("Banking_Blockchain_Survey_Responses.xlsx", index=False)
```

## Data Fields

The generated dataset includes the following fields:

- Full Name (Indian names)
- Gender
- Age Range
- Familiarity with Blockchain
- Blockchain Replacing Banking?
- Technical Challenge Significance (1-5 scale)
- Challenges in Implementing Blockchain
- Biggest Payment Processing Challenge
- Cybersecurity Risks
- Difficulty of Integration (1-5 scale)
- Financial Constraints
- Lack of Skilled Professionals (1-5 scale)
- Banking Areas Benefiting
- Primary Benefits of Blockchain
- Financial Inclusion Likelihood (1-5 scale)
- Regulatory Preparedness
- Government's Role
- Most Effective Strategy

## Output

The script generates an Excel file named "Banking_Blockchain_Survey_Responses.xlsx" containing all survey responses.

## License

[Add your chosen license here]

## Author

[Add your name/contact information here]