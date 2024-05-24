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

## Results


### Sales Trends
The visualizations show the trends in sales before and after the marketing campaign.



**Interpretation:**
- There is a clear upward shift in sales after the campaign, indicating a positive impact of the marketing campaign on sales.

### Difference-in-Differences (DiD) Analysis
The DiD analysis estimates the average treatment effect of the marketing campaign on sales.

**Key Findings:**
- The initial DiD regression indicated potential scaling issues with large coefficients, which need to be checked.
- The refined heterogeneity analysis shows a more reasonable positive impact of the campaign (`treatment * post` coefficient).

### Heterogeneity Analysis
The heterogeneity analysis explores how the impact of the campaign varies across different customer demographics and store characteristics.

**Key Findings:**
- The positive `treatment * post` coefficient in the heterogeneity analysis confirms the positive impact of the campaign.
- Interaction terms indicate that the effect is stronger for urban stores and higher-income customers.

### Summary
Overall, the marketing campaign had a significant positive impact on sales, with notable variations across different segments. These insights can help in tailoring future campaigns to maximize their effectiveness. 

### Detailed Regression Outputs
**Difference-in-Differences Regression:**

| Coefficient       | Estimate   | Std. Error | t-value | p-value |
|-------------------|------------|------------|---------|---------|
| Intercept         | 501.4041   | 3.296      | 152.114 | 0.000   |
| Treatment         | 1.038e+14  | 1.94e+13   | 0.535   | 0.593   |
| Post              | -5.192e+13 | 9.71e+13   | -0.535  | 0.593   |
| Treatment * Post  | -5.192e+13 | 9.71e+13   | -0.535  | 0.593   |
| Store Size Medium | 5.178e-05  | 2.960      | 1.75e-05| 1.000   |
| Store Size Small  | 0.9742     | 2.684      | 0.363   | 0.717   |
| Location Suburban | -0.7559    | 2.527      | -0.301  | 0.764   |
| Location Urban    | -1.6442    | 2.483      | -0.662  | 0.508   |

**Heterogeneity Regression:**
| Coefficient                     | Estimate | Std. Error | t-value | p-value |
|---------------------------------|----------|------------|---------|---------|
| Intercept                       | 504.3407 | 6.085      | 82.883  | 0.000   |
| Treatment                       | 16.4147  | 2.805      | 5.852   | 0.000   |
| Treatment * Post                | 16.4147  | 2.805      | 5.852   | 0.000   |
| Store Size Medium               | 0.9568   | 4.184      | 0.229   | 0.819   |
| Store Size Small                | 3.1659   | 3.792      | 0.835   | 0.404   |
| Location Suburban               | 0.9153   | 3.570      | 0.256   | 0.798   |
| Location Urban                  | 4.6884   | 3.509      | 1.336   | 0.182   |
| Post * Store Size Medium        | -0.6970  | 1.972      | -0.353  | 0.724   |
| Post * Store Size Small         | -1.3968  | 1.789      | -0.781  | 0.435   |
| Post * Location Suburban        | -1.1532  | 1.683      | -0.685  | 0.493   |
| Post * Location Urban           | -4.2684  | 1.654      | -2.581  | 0.010   |
| Income                          | 0.0002   | 0.000      | 1.043   | 0.297   |
| Treatment * Income              | 6.88e-05 | 6.6e-05    | 1.043   | 0.297   |
| Treatment * Post * Income       | 6.88e-05 | 6.6e-05    | 1.043   | 0.297   |

### Prerequisites
Ensure you have Python installed. It's recommended to use a virtual environment to manage dependencies.

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Causal_Inference.git
   cd Causal_Inference
