import pandas as pd
import uuid

def import_participants(path):
    df = pd.read_excel(path)

    participants = []

    for _, row in df.iterrows():
        participants.append({
            "email": row.get("email"),
            "code": f"P-{uuid.uuid4().hex[:6]}"
        })

    return participants
