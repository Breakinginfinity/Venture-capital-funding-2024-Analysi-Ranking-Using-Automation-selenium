# VC Qualification Task  

This repository contains the code and documentation for the **VC Qualification Task**, a project undertaken to evaluate and prioritize venture capital firms for Bold's fundraising outreach based on predefined fit criteria.  

## Objective  
The goal of this project was to create a system to evaluate 300+ VC firms for their fit with Bold's fundraising requirements. The task involved developing an automated qualification process with a target accuracy of 90% or higher.  

## Features  
- Automated evaluation of VC firms based on **fit** and **non-fit** criteria.  
- Proof of Concept (PoC) using Python and Pandas for a small sample size.  
- Scalable framework applied to the full list of 300+ VCs.  
- Prioritization of VCs to streamline outreach efforts.  

## Fit Criteria  
1. **Focus Area**: B2C-focused VCs investing in AI or education.  
2. **Stage**: Seed-stage investors.  
3. **Business Metrics**: Minimum ARR of $1M and international scalability.  

### Non-Fit Criteria  
- Lack of focus on B2C or Seed stage.  
- No alignment with relevant industries (AI or education).  

## Approach  
1. **Data Collection**: Extracted and validated VC information from websites and other sources.  
2. **Proof of Concept (PoC)**:  
   - Analyzed a sample batch (10-20 VCs) using Python.  
   - Automated data extraction and applied fit criteria.  
3. **Full List Evaluation**:  
   - Evaluated 300+ VCs using the PoC framework.  
   - Prioritized results to recommend outreach strategies for high-fit VCs.  

## Libraries Used  
The following libraries were utilized in this project:  
- **Pandas**: For data manipulation and analysis.  
- **Selenium**: For web scraping and automated data extraction.  
- **BeautifulSoup**: For parsing and extracting data from HTML and XML documents.  
- **Lambda Functions**: Used for concise and anonymous functions within data processing workflows.  

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/vc-qualification-task.git  
   ```  
2. Navigate to the project directory:  
   ```bash  
   cd vc-qualification-task  
   ```  
3. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

## Usage  
1. Run the PoC script to test on a small batch of VCs:  
   ```bash  
   python poc_vc_evaluation.py  
   ```  
2. Evaluate the full VC list:  
   ```bash  
   python full_vc_evaluation.py  
   ```  

## Results  
- The automated system achieved 90%+ accuracy in evaluating VC firms.  
- High-priority VCs were identified and recommended for targeted outreach.  

## Conclusion  
This project successfully demonstrated the potential for automating complex data qualification tasks, ensuring scalability and accuracy under tight time constraints.  

## License  
This project is licensed under the [MIT License](LICENSE).  
