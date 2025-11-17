# Rust CLI POC — Python BDD Integration

This repository is a **proof of concept** demonstrating how a Rust-based
command-line interface (CLI) can be controlled and tested using **Python**,
**Behave**, and **BDD-style Gherkin scenarios**.
The goal is to show how UI actions (e.g., "press play", "turn knob") can be
expressed as natural-language tests, executed via Python, and mapped to real
commands inside a Rust application.

## Overview

This project contains:
### **1. A minimal Rust CLI**
Located in `src/main.rs`, the CLI accepts simple commands such as:
- `play`
- `stop`
- `tempo`

Example:
```bash
./target/debug/rust_cli_poc play
```

Output:
```
Sequencer started.
```
This simulates a hardware/UI interaction through a CLI interface.

## Python Behave Test (BDD)
Inside the features/ directory you'll find:

- Gherkin feature file (sequencer.feature)
- Step definitions (steps.sequencer_steps.py)

A Sample scenerio:
```
  Scenario: Starting the sequencer
    When I press play
    Then I see the sequencer start
```

Behave maps these steps to Python functions that execute the Rust CLI using subprocess.run() and verify the outputs.

## Goal of the POC

This proof-of-concept shows how the project could:
- Use BDD for acceptance tests.
- Connect Python test steps to real Rust binary behavior.
- Simulate UI elements (buttons, knobs) through CLI commands.
- Provide a foundation for automated hardware/UI regression testing.
- Give non-Rust developers a natural-language interface for describing behavior.

## Setup & Usage
1. Build the Rust CLI
```cargo build```
2. Run the CLI manually
```./target/debug/rust_cli_poc play```
3. Install Poetry dependencies
```
curl -sSL https://install.python-poetry.org | python3 -
```
Then run: 
```
poetry install
```
4. Run the Behave BDD tests
```
behave
```

## Why This Approach?
- Using Python Behave + Rust CLI provides:
- A human-friendly BDD layer ("When I press play…")
- A clear interface between UI behavior and CLI commands
- Fast and portable tests
- Easy extension to hardware or embedded interfaces
- Team-friendly documentation for expected behavior
- This is a lightweight but powerful workflow to validate user interactions, end-to-end system behavior, or automated UI tests.