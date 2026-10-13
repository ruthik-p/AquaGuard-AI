import sys; sys.path.insert(0,'.')
import os, joblib
import pandas as pd

# 1. Model file
size = os.path.getsize('models/rf_model.pkl')
print(f'rf_model.pkl: {size:,} bytes')

# 2. All src imports
from src.data_loader import load_raw_data, FEATURE_COLS
from src.preprocessing import build_pipeline, get_feature_medians
from src.advisory import get_advisory, WHO_THRESHOLDS
from src.model import predict_single, predict_batch
print('All src imports: OK')

# 3. Dataset
df = load_raw_data()
print(f'Dataset: {df.shape[0]} rows x {df.shape[1]} cols')

# 4. Advisory test
sample = {
    'ph': 7.0, 'Hardness': 150.0, 'Solids': 20000.0,
    'Chloramines': 3.5, 'Sulfate': 200.0, 'Conductivity': 350.0,
    'Organic_carbon': 10.0, 'Trihalomethanes': 60.0, 'Turbidity': 3.5,
}
adv = get_advisory(0.30, sample)
print(f'Advisory tier: {adv.risk_tier}')
print(f'WHO violations: {len(adv.violations)}')
print(f'Next steps count: {len(adv.next_steps)}')

# 5. Prediction test
pipeline = joblib.load('models/rf_model.pkl')
X = pd.DataFrame([sample])[FEATURE_COLS]
prob = pipeline.predict_proba(X)[0][1]
pred = pipeline.predict(X)[0]
print(f'Sample prediction: prob={prob:.3f}, class={pred}')

# 6. Feature medians
medians = get_feature_medians(df)
print(f'Feature medians computed for {len(medians)} features')

print()
print('=== ALL CHECKS PASSED ===')
