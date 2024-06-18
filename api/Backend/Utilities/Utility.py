from flask import Flask, jsonify
from pony.orm import db_session, select
from datetime import datetime
import pandas as pd
from ..Entity.Models import InboundStock, OutboundStock


class StockAudit:
    def __init__(self):
        self.inbound_df = None
        self.outbound_df = None

    @db_session
    def fetch_data(self):

        # Fetch data from InboundStock and OutboundStock models
        inbound_data = select(i for i in InboundStock)[:]
        outbound_data = select(o for o in OutboundStock)[:]

        # Convert to DataFrame
        self.inbound_df = pd.DataFrame([item.to_dict() for item in inbound_data])
        self.outbound_df = pd.DataFrame([item.to_dict() for item in outbound_data])

    def clean_data(self):
        # Handling missing values
        self.inbound_df.dropna(inplace=True)
        self.outbound_df.dropna(inplace=True)

        # Convert date columns to datetime type
        self.inbound_df['date'] = pd.to_datetime(self.inbound_df['date'])
        self.outbound_df['date'] = pd.to_datetime(self.outbound_df['date'])

    def analyze_data(self):
        # Extract month and year from date
        self.inbound_df['month_year'] = self.inbound_df['date'].dt.to_period('M')
        self.outbound_df['month_year'] = self.outbound_df['date'].dt.to_period('M')

        # Group by month and year and sum quantities
        monthly_inbound = self.inbound_df.groupby('month_year')['quantity'].sum().reset_index()
        monthly_outbound = self.outbound_df.groupby('month_year')['quantity'].sum().reset_index()

        # Convert period to string for JSON serialization
        monthly_inbound['month_year'] = monthly_inbound['month_year'].astype(str)
        monthly_outbound['month_year'] = monthly_outbound['month_year'].astype(str)

        return {
            'monthly_inbound': monthly_inbound.to_dict(orient='records'),
            'monthly_outbound': monthly_outbound.to_dict(orient='records')
        }

    def get_audit_data(self):
        self.fetch_data()
        self.clean_data()
        return self.analyze_data()

