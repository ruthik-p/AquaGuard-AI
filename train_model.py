import sys
sys.path.insert(0, '.')
from src.data_loader import load_raw_data
from src.model import train_and_save

print('Loading data...')
df = load_raw_data()
print(f'Data loaded: {df.shape}')

print('Training model (this may take ~30 seconds)...')
metrics = train_and_save(df)

print()
print('=== TRAINING COMPLETE ===')
cv_acc_mean = metrics["cv_accuracy_mean"]
cv_acc_std  = metrics["cv_accuracy_std"]
cv_f1_mean  = metrics["cv_f1_mean"]
cv_f1_std   = metrics["cv_f1_std"]
test_acc    = metrics["test_accuracy"]
test_f1     = metrics["test_f1_macro"]

print(f'CV Accuracy : {cv_acc_mean:.4f} +/- {cv_acc_std:.4f}')
print(f'CV F1 macro : {cv_f1_mean:.4f} +/- {cv_f1_std:.4f}')
print(f'Test Accuracy: {test_acc:.4f}')
print(f'Test F1 macro: {test_f1:.4f}')
print()
print('Confusion Matrix (rows=Actual, cols=Predicted):')
cm = metrics["confusion_matrix"]
print(f'  [Not Potable] TN={cm[0][0]}  FP={cm[0][1]}')
print(f'  [Potable]     FN={cm[1][0]}  TP={cm[1][1]}')
print()
print(metrics["classification_report"])
print()
print('Feature Importances (sorted):')
fi = sorted(metrics["feature_importances"].items(), key=lambda x: x[1], reverse=True)
for feat, imp in fi:
    bar = '#' * int(imp * 100)
    print(f'  {feat:20s}: {imp:.4f}  {bar}')
