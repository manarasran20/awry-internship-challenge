# Fawry-internship-challenge
Solution for Fawry Full Stack Internship Challenge.

# Fawry Internship Challenge – Python Solution

This repository contains my solution to the Fawry Full Stack Internship Challenge, implemented in **Python**.

## Problem Summary

The task simulates a simple **e-commerce system** where a customer can:
- Add products to a cart
- Handle shipping for physical items
- Checkout with receipt and shipping breakdown

The solution includes validation for:
- Product expiration
- Out-of-stock errors
- Empty cart
- Insufficient balance

##  Features Implemented

- Product class (with expiry, weight, and shipping flags)
- Cart system for adding items
- Checkout function with:
  - Subtotal & shipping calculation
  - Error handling
  - Receipt formatting
- ShippingService to calculate total weight and print a shipment notice
- Sample test scenario at the bottom of the code

## Tech Stack

- Language: **Python**
- No external libraries required

## File Structure

- `fawry challenge.py` – main code file including product/cart system and a working example

##  How to Run

1. Make sure you have Python  installed.
2. Download or clone the repository.
3. Open terminal in the project directory and run:

```bash
python "fawry challenge.py"
