# CI-CD-PIpeline
 
This repository contains a simple web application along with a CI/CD pipeline implemented using GitHub Actions. The pipeline automates testing and deployment of the web application to Heroku.

## Running the Application Locally

To run the web application locally, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/thoshna/CI-CD-Pipeline.git
    ```

2. Navigate to the project directory:

    ```
    cd CI-CD-Pipeline
    ```

3. Install the required dependencies. Make sure you have Python installed on your system:

    ```
    pip install -r requirements.txt
    ```

4. Run the application:

    ```
    python app.py
    ```

5. Open your web browser and visit `http://localhost:5000` to view the application.

## CI/CD Pipeline Setup

The CI/CD pipeline is configured using GitHub Actions. Here's an overview of the pipeline setup:

- **Continuous Integration (CI)**:
  - On every push to the `main` branch, the pipeline triggers.
  - The pipeline checks out the code, sets up the Python environment, installs dependencies, and runs unit tests.
  - If the tests pass, the pipeline proceeds to deployment.

- **Continuous Deployment (CD)**:
  - If the tests pass, the pipeline deploys the application to Heroku.
  - Heroku API key is securely stored as a secret in the GitHub repository settings and accessed during deployment.
  - Deployment is conditional on test success to ensure only stable builds are deployed.

### GitHub Actions Workflow

The CI/CD pipeline workflow is defined in the `.github/workflows/main.yml` file in this repository. It consists of the following steps:

- Checkout code
- Set up Python environment
- Install dependencies
- Run tests
- Deploy to Heroku (if tests pass)


## Scaling for Larger Applications

The setup described here is suitable for small to medium-sized projects. For larger applications, consider the following scaling options:

- **Parallelism**: Splitting tests into parallel jobs to reduce execution time.
- **Environment Management**: Separate environments for development, staging, and production.
- **Deployment Strategies**: Implementing blue-green deployments or canary releases for zero-downtime deployments.
- **Monitoring and Logging**: Implementing monitoring and logging solutions to track application performance and detect issues.

By implementing these strategies, the CI/CD pipeline can effectively scale to meet the needs of larger and more complex applications.
