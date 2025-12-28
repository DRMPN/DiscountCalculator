# DiscountCalculator

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

## Overview

This project provides a secure platform for clients to manage their contracts and calculate dynamic early payment discounts. It enables users to register, view contract details, and generate early payment proposals based on custom inputs, offering a clear financial benefit for timely payments.

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

## Core features

1.  **User Authentication and Authorization**: The application provides a secure login system for clients using INN (Individual Taxpayer Number) and password, including password hashing for security. It also features a two-factor authentication step with a hardcoded code '1234' after initial login. User sessions are managed to ensure only logged-in users can access protected routes.
2.  **Client Registration**: New clients can register for an account by providing their INN, email, and a password. The system checks for existing INNs and ensures password confirmation matches before creating a new client entry in the database.
3.  **Contract Management and Display**: Authenticated clients can view a list of their contracts, including details such as contract number, subject, price, and date. This information is retrieved from a SQLite database and presented in a user-friendly format.
4.  **Dynamic Discount Calculation**: The core functionality allows users to input a desired early payment date and amount. The system then calculates a dynamic discount percentage for each of their contracts based on a complex formula involving contract dates, desired payment amount, maximum early payment sum, annual deposit rate, and operational costs.
5.  **Early Payment Proposal Generation**: After calculating the dynamic discount, the application generates a proposal for each contract, displaying the original contract details, the user-specified early payment date and amount, the calculated discount percentage, and the resulting 'our price' (discounted price).

## Installation

Install DiscountCalculator using one of the following methods:

**Build from source:**

1.  Clone the DiscountCalculator repository:

    ```sh
    git clone https://github.com/DRMPN/DiscountCalculator
    ```

2.  Navigate to the project directory:

    ```sh
    cd DiscountCalculator
    ```

3.  Install the project dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Contributing

-   **[Report Issues](https://github.com/DRMPN/DiscountCalculator/issues)**: Submit bugs found or log feature requests for the project.

## Citation

If you use this software, please cite it as below.

### APA format:

    DRMPN (2022). DiscountCalculator repository [Computer software]. https://github.com/DRMPN/DiscountCalculator

### BibTeX format:

    @misc{DiscountCalculator,

        author = {DRMPN},

        title = {DiscountCalculator repository},

        year = {2022},

        publisher = {github.com},

        journal = {github.com repository},

        howpublished = {\url{https://github.com/DRMPN/DiscountCalculator.git}},

        url = {https://github.com/DRMPN/DiscountCalculator.git}

    }