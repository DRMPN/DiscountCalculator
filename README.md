# DiscountCalculator

---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

---

## Overview

DiscountCalculator helps clients of Gazprom Neft understand potential discounts on contracts. Users securely log in to view their contracts and calculate dynamic discount options based on contract details and desired payout amounts, facilitating informed financial decisions.

---

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

---
## Core features

1. **User Authentication**: Allows users to log in securely using their INN and password, with an additional two-factor authentication code. Also includes user registration functionality.
2. **Contract Management**: Stores and displays a list of contracts associated with each client, including details like contract number, subject, price, and completion date.
3. **Discount Calculation**: Calculates dynamic discounts based on the contract's completion date, desired payout amount, and other parameters using a defined formula. The result is displayed to the user.
4. **Data Persistence**: Uses an SQLite database (finance.db) to store client information and contract details, ensuring data is saved between sessions.
5. **Session Management**: Manages user sessions using Flask-Session, allowing users to remain logged in while navigating the application. Uses cookies for temporary authentication before session is established.

---

## Installation

Install DiscountCalculator using one of the following methods:

**Build from source:**

1. Clone the DiscountCalculator repository:
```sh
git clone https://github.com/DRMPN/DiscountCalculator
```

2. Navigate to the project directory:
```sh
cd DiscountCalculator
```

3. Install the project dependencies:

```sh
pip install -r requirements.txt
```

---

## Contributing

- **[Report Issues](https://github.com/DRMPN/DiscountCalculator/issues)**: Submit bugs found or log feature requests for the project.

---

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

---
