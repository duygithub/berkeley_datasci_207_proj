import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import kagglehub

def show_default_loans():     
    df['recovery_ratio'] = df['total_pymnt'] / df['loan_amnt']
    
    charged_off_loans = df[df['loan_status'] == 'Charged Off'].copy()
