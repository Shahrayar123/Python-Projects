# Email Processor

This script processes unread emails, extracts relevant information, and updates an Excel file accordingly.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/coast-moonlight/email_processor.git
    cd email-processor
    ```

2. **Install dependencies**:
    ```bash
    pip install openpyxl langdetect googletrans==4.0.0-rc1
    ```

3. **Create a configuration file**:
    - Copy `config_example.json` to `config.json`.
    - Update `config.json` with your email credentials and the path to the Excel file.

4. **Set environment variable (optional)**:
    ```bash
    export CONFIG_FILE=config.json
    ```

## Running the Script

```bash
python email_processor.py
```