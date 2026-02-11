import numpy as np
import pandas as pd
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Define project paths
project_root = Path(__file__).resolve().parents[1]
raw_data_path = project_root / "data" / "raw"
raw_data_path.mkdir(parents=True, exist_ok=True)

# Create users dataset
n_users = 1000

signup_dates = (
    pd.to_datetime("2025-01-01")
    + pd.to_timedelta(np.random.randint(0, 90, n_users), unit="D")
)

users = pd.DataFrame({
    "user_id": ["U" + str(i).zfill(4) for i in range(1, n_users + 1)],
    "signup_date": signup_dates,
    "device": np.random.choice(["iOS", "Android", "Web"], n_users),
    "country": np.random.choice(["UK", "US", "Canada"], n_users),
    "acquisition_channel": np.random.choice(
        ["Organic", "Ads", "Referral"], n_users
    ),
})

# Define feature launch date
feature_launch_date = pd.to_datetime("2025-03-15")

# Create events dataset
events_list = []

for user_id in users["user_id"]:
    n_events = np.random.randint(3, 8)

    event_dates = (
        pd.to_datetime("2025-01-01")
        + pd.to_timedelta(np.random.randint(0, 120, n_events), unit="D")
    )

    for event_time in event_dates:
        event_name = np.random.choice(["login", "browse", "purchase"])

        if event_name == "purchase":
            order_value = round(float(np.random.uniform(5, 120)), 2)
        else:
            order_value = np.nan

        events_list.append([user_id, event_time, event_name, order_value])

    if np.random.rand() < 0.4:
        adopt_date = (
            feature_launch_date
            + pd.to_timedelta(np.random.randint(0, 30), unit="D")
        )
        events_list.append([user_id, adopt_date, "feature_used", np.nan])

events = pd.DataFrame(
    events_list,
    columns=["user_id", "event_time", "event_name", "order_value"],
)

# Enforce 4-digit event IDs (max 9999 events)
if len(events) > 9999:
    raise ValueError(
        f"Too many events ({len(events)}). Reduce events to stay <= 9999."
    )

events.insert(
    0,
    "event_id",
    ["E" + str(i).zfill(4) for i in range(1, len(events) + 1)],
)

# Save datasets
users.to_csv(raw_data_path / "users.csv", index=False)
events.to_csv(raw_data_path / "events.csv", index=False)

print("Dataset generated successfully!")
print("Users shape:", users.shape)
print("Events shape:", events.shape)
print("Events columns:", list(events.columns))

