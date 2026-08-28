KEYWORDS = ["abs", "sixpack", "kiss", "stains", "shading", "dcua", "muscle", "collarbone"]

def check_list(detection_reasons, detected_keywords):
    return (True, detection_reasons, detected_keywords) if detection_reasons else (False, "No detections", [])

def filter_asset_name(asset_name: str):
    asset_name_lowered = asset_name.lower()
    words = asset_name_lowered.split(" ")

    detected_keywords = []
    detection_reasons = []

    for word in words:
        if word in KEYWORDS:
            detected_keywords.append(word)
            detection_reasons.append("Slop keyword in asset name")

    if len(detected_keywords) > 2:
        detection_reasons.append("More than two slop keywords in asset name")

    return check_list(detection_reasons, detected_keywords)