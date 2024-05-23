# Impact of a Multichannel Marketing Campaign

This project evaluates the causal impact of a multichannel marketing campaign on sales using the difference-in-differences (DiD) method. The analysis also explores the heterogeneity of the campaign's impact across different customer demographics and store characteristics.

## Project Structure

- **data/**: Contains the simulated data files used in the analysis.
- **notebooks/**: Contains Jupyter notebooks for data exploration and analysis.
- **src/**: Contains Python scripts for data simulation.
- **README.md**: Project documentation.
- **requirements.txt**: List of project dependencies.

## Project Description

### Objective
Evaluate the causal impact of a multichannel marketing campaign on sales and understand how this impact varies across different customer segments and store locations.

### Data
The data used in this project is simulated and includes:
- **sales_before.csv**: Daily sales data before the campaign, including `store_id`, `customer_id`, and `sales`.
- **sales_after.csv**: Daily sales data after the campaign, including `store_id`, `customer_id`, and `sales`.
- **store_characteristics.csv**: Information about store characteristics (`store_id`, `store_size`, `store_location`).
- **customer_demographics.csv**: Demographic information about customers (`customer_id`, `age`, `gender`, `income`).

### Methodology
1. **Data Simulation**: Generate simulated sales, store characteristics, and customer demographics data.
2. **Data Exploration**: Perform preliminary analysis to understand the data structure and key features.
3. **DiD Analysis**: Apply the difference-in-differences method to estimate the causal impact of the marketing campaign.
4. **Heterogeneity Analysis**: Evaluate how the campaign's impact varies across different customer demographics and store characteristics.

### Results
The results will be presented in terms of effect estimates and visualizations showing sales trends before and after the campaign, and how this effect varies across segments.

## Usage

### Prerequisites
Ensure you have Python installed. It's recommended to use a virtual environment to manage dependencies.

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Causal_Inference.git
   cd Causal_Inference
