<!-- Back to top link -->
<a name="readme-top"></a>

[![Python][Python.shield]][Python-url]
[![Selenium][Selenium.shield]][Selenium-url]
[![Pytest][Pytest.shield]][Pytest-url]
[![POM][POM.shield]][POM-url]

<br />
<div align="center">
  <h1 align="center">Flyr QA Automation Technical Test</h1>

  <p align="center">
    Solution for the Flyr QA Automation technical test, demonstrating web automation skills and programming knowledge.
    <br />
    <br />
    <a href="#about">About The Project</a>
    ·
    <a href="#installation">Installation</a>
    ·
    <a href="#usage">Usage</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About The Project</a></li>
    <li>
      <a href="#project-structure">Project Structure</a>
      <ul>
        <li><a href="#pom-architecture">POM Architecture</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#test-scenarios">Test Scenarios</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About

This repository contains the solution for the Flyr QA Automation technical test. The project demonstrates automation capabilities and programming skills through three main components:

1. Algorithm exercises (FooBar and Happy Number)
2. Python programming challenges
3. Web automation suite for Avianca's website (https://www.avianca.com)

The web automation component is built using Selenium WebDriver with Python, following the Page Object Model (POM) design pattern for better maintainability and reusability.

<p align="right">(<a href="#readme-top">Back to top</a>)</p>

## Project Structure


├── PrimerPunto/
│   └── FooBar.py
├── SegundoPunto/
│   └── numeroFeliz.py
├── TercerPunto/
│   ├── pages/
│   │   ├── flightPage.py
│   │   ├── homePage.py
│   │   ├── passengersPage.py
│   │   ├── paymentPage.py
│   │   ├── seatmapPage.py
│   │   └── servicesPage.py
│   ├── tests/
│   │   ├── testBookingOneWay.py
│   │   ├── testBookingRoundTrip.py
│   │   ├── testFooter.py
│   │   ├── testHeaderRedirections.py
│   │   ├── testLanguageChange.py
│   │   └── testPOS.py
│   ├── utils/
│   │   ├── helpers.py
│   │   ├── localStorage.py
│   │   └── printer.py
│   ├── requirements.txt
│   └── README.md


### POM Architecture

The project implements the Page Object Model (POM) design pattern, which is a design pattern commonly used in test automation. It creates an object repository for storing all web elements and helps reduce code duplication and improves test maintenance.

Learn more about POM: [Selenium Documentation - Page Object Models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

<p align="right">(<a href="#readme-top">Back to top</a>)</p>

## Getting Started

### Prerequisites

* Python 3.7 or higher
* pip (Python package installer)
* Chrome or Firefox browser

### Installation

1. Clone the repository
   sh
   git clone https://github.com/DanielFAdarve/Flyr/
   cd Flyr
   

2. For PrimerPunto and SegundoPunto:
   sh
   # No additional installation required
   

3. For TercerPunto:
   sh
   cd TercerPunto
   python -m venv flyr
   .\flyr\Scripts\activate # For windows enviroments
   pip install -r requirements.txt
   

<p align="right">(<a href="#readme-top">Back to top</a>)</p>

## Usage

### Running Algorithm Exercises

1. FooBar Exercise:
   sh
   cd PrimerPunto
   python FooBar.py
   

2. Happy Number Exercise:
   sh
   cd SegundoPunto
   python numeroFeliz.py
   

### Running Web Automation Tests

1. Activate the virtual environment:
   sh
   cd TercerPunto
   .\flyr\Scripts\activate # For windows enviroments
   

2. Run specific tests:
   sh
   cd tests
   pytest testBookingOneWay.py  # Run one-way booking tests
   pytest testBookingRoundTrip.py  # Run round-trip booking tests
   pytest  # Run all tests
   

<p align="right">(<a href="#readme-top">Back to top</a>)</p>

## Test Scenarios

The automation suite covers the following scenarios:

* One-way and round-trip flight bookings
* Footer functionality testing
* Header redirections verification
* Language change functionality
* Point of Sale (POS) testing
* Complete booking flow including:
  * Flight selection
  * Passenger information
  * Seat selection
  * Additional services
  * Payment process

<p align="right">(<a href="#readme-top">Back to top</a>)</p>

## Contributing and comments

Contributions are welcome! Please feel free to submit any comments.

## License

This is a semi private project, create for Flyr. All rights reserved.

<p align="right">(<a href="#readme-top">Back to top</a>)</p>

[Python.shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Selenium.shield]: https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
[Pytest.shield]: https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/
[POM.shield]: https://img.shields.io/badge/POM-FF6B6B?style=for-the-badge
[POM-url]: https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge
[license-url]: https://opensource.org/licenses/MIT