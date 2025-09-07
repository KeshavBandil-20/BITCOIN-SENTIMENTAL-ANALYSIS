# Bitcoin Sentiment Analysis & Real-Time Market Impact System

## Overview
This repository contains a system to analyze Bitcoin sentiment from historical and real-time tweets , predict price movement, and provide alerts.

## Installation
```bash
pip install -r requirements.txt
```
## Usage
- Run historical analysis: `python src/prediction_model.py`
- Start dashboard: `streamlit run src/dashboard.py`
- Start real-time influencer stream: `python src/real_time_stream.py`
- Alerts are triggered automatically when sentiment exceeds threshold.

## Configuration
Edit `config.py` to add your Twitter API keys, influencer IDs, and email settings.
